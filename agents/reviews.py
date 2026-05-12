from agents import llm_client
from agents import llm_client
from agents import llm_client
from agents import llm_client
import os
import json
# pyrefly: ignore [missing-import]
import pandas as pd
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

from agents.llm_client import call_cerebras, retry_with_backoff

load_dotenv()

def load_business(business_path, business_id):
    """
    Finds a specific business by ID from the Yelp business file.
    Reads line by line so i never load the whole file into memory.
    """
    with open(business_path, 'r', encoding='utf-8') as f:
        for line in f:
            business = json.loads(line)
            if business['business_id'] == business_id:
                return business
    return None


def find_businesses_by_category(business_path, category, limit=5):
    """
    Finds businesses matching a category keyword.
    Used to find relevant businesses for a user to review.
    """
    matches = []
    with open(business_path, 'r', encoding='utf-8') as f:
        for line in f:
            business = json.loads(line)
            if (business.get('categories') and
                    category.lower() in business['categories'].lower() and
                    business.get('review_count', 0) > 20):
                matches.append(business)
            if len(matches) >= limit:
                break
    return matches


def profile_business(business):
    """
    Extracts the signals that matter for a user collision analysis.
    Not everything though, just what a real person would react to.
    """
    attributes = business.get('attributes') or {}

    price_range = attributes.get('RestaurantsPriceRange2', 'unknown')
    price_map = {'1': 'cheap', '2': 'mid-range', '3': 'upscale', '4': 'fine dining'}
    price_label = price_map.get(str(price_range), 'unknown price range')

    has_wifi = 'wifi' in str(attributes).lower()
    outdoor_seating = attributes.get('OutdoorSeating', 'False') == 'True'
    takes_reservations = attributes.get('RestaurantsReservations', 'False') == 'True'
    good_for_groups = attributes.get('RestaurantsGoodForGroups', 'False') == 'True'
    alcohol = attributes.get('Alcohol', '')
    noise_level = attributes.get('NoiseLevel', '')
    ambiance = attributes.get('Ambience', '')

    hours = business.get('hours') or {}
    late_night = any(
        int(close.split(':')[0]) >= 22
        for close in hours.values()
        if close and ':' in close
    )

    return {
        'business_id': business['business_id'],
        'name': business['name'],
        'categories': business.get('categories', ''),
        'city': business.get('city', ''),
        'state': business.get('state', ''),
        'overall_rating': business.get('stars', 0),
        'review_count': business.get('review_count', 0),
        'is_open': business.get('is_open', 0),
        'price_range': price_label,
        'has_wifi': has_wifi,
        'outdoor_seating': outdoor_seating,
        'takes_reservations': takes_reservations,
        'good_for_groups': good_for_groups,
        'alcohol': alcohol,
        'noise_level': noise_level,
        'ambiance': ambiance,
        'open_late': late_night
    }


@retry_with_backoff
def collision_analysis(persona, business_profile, painpoints=None):
    """
    The reasoning layer.
    Finds where this user's values and this business's signals collide; 
    what they'll love, what they won't tolerate, what the business needs to fix.

    When painpoints are provided, the analysis is grounded in real customer feedback
    rather than generic observations.
    """
    # Build painpoint context if available
    painpoint_context = ""
    if painpoints and (painpoints.get('complaints') or painpoints.get('praise')):
        complaint_lines = []
        for c in painpoints.get('complaints', [])[:5]:
            quotes = ', '.join(f'"{q}"' for q in c.get('quotes', [])[:2])
            complaint_lines.append(f"  - {c['theme']} (mentioned {c.get('frequency', c.get('count', '?'))}x, severity: {c.get('severity', '?')}). Customers said: {quotes}")

        praise_lines = []
        for p in painpoints.get('praise', [])[:5]:
            quotes = ', '.join(f'"{q}"' for q in p.get('quotes', [])[:2])
            praise_lines.append(f"  - {p['theme']} (mentioned {p.get('frequency', p.get('count', '?'))}x). Customers said: {quotes}")

        painpoint_context = f"""

REAL CUSTOMER FEEDBACK FROM THIS BUSINESS:
Complaints:
{chr(10).join(complaint_lines) if complaint_lines else '  None identified'}

Praise:
{chr(10).join(praise_lines) if praise_lines else '  None identified'}

IMPORTANT: Your analysis MUST reference these real customer complaints and praise.
Do not give generic advice. Cite specific customer language when possible.
"""

    # Build grounding quotes context if persona has them
    grounding_context = ""
    if persona.get('grounding_quotes'):
        quotes = '\n'.join(f'  - "{q}"' for q in persona['grounding_quotes'][:3])
        grounding_context = f"\nGROUNDING QUOTES (actual reviews from customers like this):\n{quotes}\n"

    prompt = f"""
You are a customer behavior analyst. You have a deep profile of a real customer
and the details of a business they have never visited.

Your job is to reason through how this specific customer will experience this business,  
not generically, but based on exactly WHO they are.

CUSTOMER PROFILE:
{persona['narrative']}
{grounding_context}
DRIFT OBSERVED:
{chr(10).join(persona['structured']['drifts']) if persona['structured']['drifts'] else 'No significant drift'}

RECENT BEHAVIOR:
- Average recent rating: {persona['structured']['phases']['recent']['signal']['avg_rating']}
- What they keep talking about: {', '.join(persona['structured']['phases']['recent']['signal']['top_words'][:8])}

BUSINESS:
- Name: {business_profile['name']}
- Type: {business_profile['categories']}
- Location: {business_profile['city']}, {business_profile['state']}
- Overall rating on Yelp: {business_profile['overall_rating']} ({business_profile['review_count']} reviews)
- Price range: {business_profile['price_range']}
- Outdoor seating: {business_profile['outdoor_seating']}
- Open late: {business_profile['open_late']}
- Takes reservations: {business_profile['takes_reservations']}
- Alcohol served: {business_profile['alcohol']}
- Noise level: {business_profile['noise_level']}
{painpoint_context}
Reason through THREE things:

1. MATCH POINTS — what specifically about this business will resonate with this customer
based on their history and values. Be very specific.

2. FRICTION POINTS — where is this business most likely to disappoint this customer.
What are the landmines given who they are and what they punish.

3. BUSINESS ADVISORY — in 2 sentences, tell this business exactly what they need
to fix or emphasize to retain this type of customer. This is the actionable intelligence.

Be sharp. Be on point. Be specific. Not generic observations.
{'Reference actual customer quotes where relevant.' if painpoints else ''}
"""

    return call_cerebras(
        prompt=prompt,
        system_prompt="You are a sharp, data-driven customer behavior analyst. Be specific, not generic.",
        temperature=0.7,
        max_tokens=1500,
    )

def generate_review(persona, business_profile, collision, sample_reviews):
    """
    Use the collision analysis to write the review and predict the rating.
    Passes actual sample reviews so the LLM mimics real writing, not a description of it.
    """
    
    samples_text = "\n\n---\n\n".join(sample_reviews[:3])
    
    prompt = f"""
You are going to write a Yelp review impersonating a specific real person.
Below are 8 actual reviews they wrote, ordered from oldest to most recent.
Read every single one before you write anything.

THEIR ACTUAL REVIEWS from oldest to most recent:

REVIEW 1 (early):
{sample_reviews[0] if len(sample_reviews) > 0 else ''}

REVIEW 2 (early):
{sample_reviews[1] if len(sample_reviews) > 1 else ''}

REVIEW 3 (middle):
{sample_reviews[2] if len(sample_reviews) > 2 else ''}

REVIEW 4 (middle):
{sample_reviews[3] if len(sample_reviews) > 3 else ''}

REVIEW 5 (middle):
{sample_reviews[4] if len(sample_reviews) > 4 else ''}

REVIEW 6 (recent):
{sample_reviews[5] if len(sample_reviews) > 5 else ''}

REVIEW 7 (recent):
{sample_reviews[6] if len(sample_reviews) > 6 else ''}

REVIEW 8 (recent):
{sample_reviews[7] if len(sample_reviews) > 7 else ''}

Now study what you just read. Notice:

1. They never open with "I stopped by" or "I finally checked out" or "I just got back."
   They open with a take; something they already believe before they walked in.
   Sometimes it's a confession. Sometimes it's a cultural reference. 
   Sometimes it's a statement about the world that leads into this specific place.

2. Their sentences run long and double back on themselves. 
   They use parentheses to add asides mid thought.
   They correct themselves out loud.
   They address the reader directly sometimes; "and let me tell you" or "I mean come on."

3. They praise with specific details, never adjectives alone.
   They don't say "the food was great." They say what specifically made it great
   and why that specific thing mattered to them personally.

4. When they complain, they explain the principle behind the complaint.
   It's never just "the service was slow." It's slow service as evidence of something
   they believe about how businesses should operate.

5. Their recent reviews are more measured than their early ones.
   More specific. Less hyperbolic. But the voice is the same underneath.

NOW...write a review of this business as this person:

WHAT THEY WOULD ENCOUNTER AT THIS BUSINESS:
{collision}

BUSINESS:
{business_profile['name']} — {business_profile['categories']} — {business_profile['city']}, {business_profile['state']}

Hard rules:
- Open with a take or declaration, not with arriving at the place
- Write 200-300 words, not more
- Use their actual sentence rhythm, their long, winding, self correcting
- Be specific to this exact business and city
- Do not mention any past review they wrote by name
- Do not repeat anything from other reviews in this session

REVIEW:
[write it here]

PREDICTED RATING: [X]/5
[just one sentence on what specifically tipped it to that number]

EARLY WARNING TO BUSINESS OWNER:
[two sharp, very specific sentences about what this customer type will write publicly 
in 6 months if current patterns hold]
"""
    

    response = client.chat.completions.create(  
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.75,
        max_tokens=800
    )

    return response.choices[0].message.content

def run(persona, business_path, business_id=None, category=None):
    if business_id:
        business = load_business(business_path, business_id)
        if not business:
            print(f"Business {business_id} not found.")
            return None
        businesses = [business]
    elif category:
        businesses = find_businesses_by_category(business_path, category)
        if not businesses:
            print(f"No businesses found for category: {category}")
            return None
    else:
        print("Provide either a business_id or a category.")
        return None

    def get_phase_samples(phase_signal, n=3):
        if not phase_signal or not phase_signal.get('sample_texts'):
            return []
        return phase_signal['sample_texts'][:n]

    early_samples = get_phase_samples(
        persona['structured']['phases']['early']['signal'], n=2
    )
    middle_samples = get_phase_samples(
        persona['structured']['phases']['middle']['signal'], n=3
    )
    recent_samples = get_phase_samples(
        persona['structured']['phases']['recent']['signal'], n=3
    )

    sample_reviews = early_samples + middle_samples + recent_samples

    results = []
    for business in businesses:
        profile = profile_business(business)
        print(f"\nAnalyzing: {profile['name']}")

        collision = collision_analysis(persona, profile)
        prediction = generate_review(persona, profile, collision, sample_reviews)

        results.append({
            'business': profile,
            'collision_analysis': collision,
            'prediction': prediction
        })

    return results


if __name__ == "__main__":
    print("starting")
    import json

    # load the persona we already built
    persona_path = 'outputs/bJ5FtCtZX3ZZacz2_2PJjA_persona.json'
    with open(persona_path, 'r') as f:
        raw = json.load(f)

    persona = {
        'structured': raw['structured'],
        'narrative': raw['narrative']
    }

    results = run(
        persona=persona,
        business_path='data/yelp_academic_dataset_business.json',
        category='Bar'
    )

    if results:
        for r in results:
            print(f"\n{'='*60}")
            print(f"BUSINESS: {r['business']['name']}")
            print(f"\nCOLLISION ANALYSIS:\n{r['collision_analysis']}")
            print(f"\nPREDICTION:\n{r['prediction']}")

        # save
        os.makedirs('outputs', exist_ok=True)
        with open('outputs/review_predictions.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print("\nSaved to review_predictions.json") 