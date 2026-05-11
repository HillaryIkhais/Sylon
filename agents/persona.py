import os
import json
import pandas as pd
import numpy as np
from google import genai
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def split_into_phases(reviews_df):
    """
    Split a user's review history into three life phases:
    early, middle, recent.
    Not equal splits, weighted toward recency.
    """
    reviews_df = reviews_df.sort_values('date').reset_index(drop=True)
    n = len(reviews_df)

    early = reviews_df.iloc[:n//3]
    middle = reviews_df.iloc[n//3: 2*n//3]
    recent = reviews_df.iloc[2*n//3:]

    return early, middle, recent


def extract_phase_signal(phase_df):
    """
    For a given phase, extracts the raw signals that's necessary:
    average rating, rating variance, most used words, sample texts.
    """
    if phase_df.empty:
        return None

    ratings = phase_df['stars'].tolist()
    texts = phase_df['text'].tolist()

    # word frequency, skip short words
    word_counts = defaultdict(int)
    for text in texts:
        for word in text.lower().split():
            if len(word) > 4:
                word_counts[word] += 1

    top_words = sorted(word_counts, key=word_counts.get, reverse=True)[:15]

    # find the reviews with the biggest gap between text length and rating
    phase_df = phase_df.copy()
    phase_df['text_length'] = phase_df['text'].apply(lambda x: len(x.split()))
    phase_df['normalized_rating'] = (phase_df['stars'] - 1) / 4
    phase_df['gap'] = phase_df['text_length'] * abs(phase_df['normalized_rating'] - 0.5)
    gap_reviews = phase_df.nlargest(2, 'gap')[['stars', 'text']].to_dict('records')

    # sample texts for LLM context, to pick the longest ones
    sample_texts = phase_df.nlargest(3, 'text_length')['text'].tolist()

    return {
        'review_count': len(phase_df),
        'avg_rating': round(np.mean(ratings), 2),
        'rating_variance': round(np.var(ratings), 2),
        'top_words': top_words,
        'gap_reviews': gap_reviews,
        'sample_texts': sample_texts
    }


def detect_drift(early_signal, middle_signal, recent_signal):
    """
    Compares signals across phases to find what changed.
    Returns a plain description of the drift.
    """
    drifts = []

    if early_signal and recent_signal:
        rating_change = recent_signal['avg_rating'] - early_signal['avg_rating']
        if abs(rating_change) > 0.5:
            direction = "more generous" if rating_change > 0 else "harsher"
            drifts.append(f"Rating drift: became {direction} over time ({early_signal['avg_rating']} to {recent_signal['avg_rating']})")

        # word overlap between early and recent
        early_words = set(early_signal['top_words'])
        recent_words = set(recent_signal['top_words'])
        lost_words = early_words - recent_words
        gained_words = recent_words - early_words

        if lost_words:
            drifts.append(f"Stopped emphasizing: {', '.join(list(lost_words)[:5])}")
        if gained_words:
            drifts.append(f"Started emphasizing: {', '.join(list(gained_words)[:5])}")

    return drifts


def build_structured_persona(user_id, early, middle, recent, drifts):
    """
    Assembles the structured part of the persona,
    the labeled sections the rest of the pipeline reads.
    """
    return {
        'user_id': user_id,
        'phases': {
            'early': {
                'period': f"{early['date'].min()} → {early['date'].max()}" if not early.empty else None,
                'signal': extract_phase_signal(early)
            },
            'middle': {
                'period': f"{middle['date'].min()} → {middle['date'].max()}" if not middle.empty else None,
                'signal': extract_phase_signal(middle)
            },
            'recent': {
                'period': f"{recent['date'].min()} → {recent['date'].max()}" if not recent.empty else None,
                'signal': extract_phase_signal(recent)
            }
        },
        'drifts': drifts
    }


def build_narrative_persona(structured_persona, user_id):
    """
    Feeds the structured persona into Gemini and asks it to write
    a character description; the human readable section.
    """
    prompt = f"""
You are reading the behavioral data of a real person extracted from their Yelp review history.
Your job is to write a sharp, on point and specific character portrait of this reviewer.

Do not be generic. Do not say things like "this user enjoys dining out."
Write like you actually know this person personally; their quirks, their priorities, their blind spots.

Here is their behavioral data:

EARLY PHASE ({structured_persona['phases']['early']['period']}):
- Average rating: {structured_persona['phases']['early']['signal']['avg_rating']}
- Rating variance: {structured_persona['phases']['early']['signal']['rating_variance']}
- Most used words: {', '.join(structured_persona['phases']['early']['signal']['top_words'])}
- Sample reviews: {json.dumps(structured_persona['phases']['early']['signal']['sample_texts'][:2])}

RECENT PHASE ({structured_persona['phases']['recent']['period']}):
- Average rating: {structured_persona['phases']['recent']['signal']['avg_rating']}
- Rating variance: {structured_persona['phases']['recent']['signal']['rating_variance']}
- Most used words: {', '.join(structured_persona['phases']['recent']['signal']['top_words'])}
- Sample reviews: {json.dumps(structured_persona['phases']['recent']['signal']['sample_texts'][:2])}

OBSERVED DRIFTS:
{chr(10).join(structured_persona['drifts']) if structured_persona['drifts'] else 'No significant drift detected'}

Write a 150-200 word character portrait. Be specific. Be sharp. No fluff.
End with one sentence that captures what this person would never forgive in a bad experience.
"""

    response =client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text


def excavate_user(user_id, reviews_df):
    """
    Main function. Takes a user ID and their reviews,
    returns both their structured and narrative persona.
    """
    user_reviews = reviews_df[reviews_df['user_id'] == user_id].copy()
    user_reviews['date'] = pd.to_datetime(user_reviews['date'])

    early, middle, recent = split_into_phases(user_reviews)

    early_signal = extract_phase_signal(early)
    middle_signal = extract_phase_signal(middle)
    recent_signal = extract_phase_signal(recent)

    drifts = detect_drift(early_signal, middle_signal, recent_signal)

    structured = build_structured_persona(user_id, early, middle, recent, drifts)
    narrative = build_narrative_persona(structured, user_id)

    return {
        'structured': structured,
        'narrative': narrative
    }


if __name__ == "__main__":
    df = pd.read_csv('data/sampled_reviews.csv')

    # to test on the highest scored user
    top_user = df.sort_values('richness_score', ascending=False).iloc[0]['user_id']
    print(f"Excavating user: {top_user}\n")

    persona = excavate_user(top_user, df)

    print("STRUCTURED PERSONA")
    print(json.dumps(persona['structured'], indent=2, default=str))
    print("\n NARRATIVE PERSONA")
    print(persona['narrative'])

    # to save it
    os.makedirs('outputs', exist_ok=True)
    with open(f'outputs/{top_user}_persona.json', 'w') as f:
        json.dump(persona, f, indent=2, default=str)

    print(f"\nSaved to outputs{top_user}_persona.json")