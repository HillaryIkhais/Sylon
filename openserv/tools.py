import os
import sys
import json
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.persona import excavate_user
from agents.reviews import collision_analysis
from agents.persona_factory import generate_synthetic_personas
from agents.google_places import fetch_competitor_personas
from agents.review_ingest import ingest_text, ingest_json, ingest_csv, load_reviews
from agents.painpoint_extractor import (
    extract_painpoints,
    excavate_personas_from_reviews,
    load_painpoints,
    load_personas,
)

_REVIEWS_DF = None

def get_reviews_df():
    global _REVIEWS_DF
    if _REVIEWS_DF is None:
        try:
            _REVIEWS_DF = pd.read_csv('data/sampled_reviews.csv')
            _REVIEWS_DF['date'] = pd.to_datetime(_REVIEWS_DF['date'])
        except FileNotFoundError:
            print("Warning: data/sampled_reviews.csv not found.")
            _REVIEWS_DF = pd.DataFrame()
    return _REVIEWS_DF

def tool_excavate_persona(user_id: str) -> dict:
    df = get_reviews_df()
    if df.empty or user_id not in df['user_id'].values:
        return {"error": f"User {user_id} not found in the dataset."}
    return excavate_user(user_id, df)

def tool_run_collision_simulation(
    persona_narrative, persona_drifts, recent_rating, top_words,
    business_attributes, painpoints=None, grounding_quotes=None,
) -> str:
    mock_persona = {
        'narrative': persona_narrative,
        'structured': {
            'drifts': persona_drifts,
            'phases': {'recent': {'signal': {'avg_rating': recent_rating, 'top_words': top_words}}}
        }
    }
    if grounding_quotes:
        mock_persona['grounding_quotes'] = grounding_quotes

    profile = {
        'name': business_attributes.get('name', 'Unknown Business'),
        'categories': business_attributes.get('categories', 'Restaurant'),
        'city': business_attributes.get('city', 'Unknown City'),
        'state': business_attributes.get('state', 'Unknown State'),
        'overall_rating': business_attributes.get('overall_rating', 'N/A'),
        'review_count': business_attributes.get('review_count', 'N/A'),
        'price_range': business_attributes.get('price_range', 'unknown'),
        'outdoor_seating': business_attributes.get('outdoor_seating', False),
        'takes_reservations': business_attributes.get('takes_reservations', False),
        'alcohol': business_attributes.get('alcohol', 'none'),
        'noise_level': business_attributes.get('noise_level', 'average'),
        'open_late': business_attributes.get('open_late', False)
    }
    return collision_analysis(mock_persona, profile, painpoints=painpoints)

def tool_generate_synthetic_personas(business_description, location="", count=3):
    return generate_synthetic_personas(business_description, location, count)

def tool_fetch_competitor_personas(business_category, location="", limit=2):
    return fetch_competitor_personas(business_category, location, limit)

def tool_ingest_reviews(business_id, reviews_text=None, reviews_json=None, csv_path=None):
    if reviews_text:
        return ingest_text(reviews_text, business_id)
    elif reviews_json:
        return ingest_json(reviews_json, business_id)
    elif csv_path:
        return ingest_csv(csv_path, business_id)
    return []

def tool_extract_painpoints(business_id):
    reviews = load_reviews(business_id)
    if not reviews:
        return {"painpoints": {}, "personas": [], "review_count": 0}
    painpoints = extract_painpoints(reviews, business_id)
    personas = excavate_personas_from_reviews(reviews, painpoints, business_id)
    return {"painpoints": painpoints, "personas": personas, "review_count": len(reviews)}
