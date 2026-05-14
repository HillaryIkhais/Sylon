"""
Phase 2: Google Places Review Fetcher

Pulls real customer reviews from Google Maps for competitor businesses
near the owner's location, then excavates behavioral personas from them.
"""
import os
import json
import requests
# pyrefly: ignore [missing-import]
from google import genai    
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY", "")


def search_nearby_competitors(query: str, location: str = "", limit: int = 3) -> list:
    """
    Uses Google Places Text Search to find competitor businesses.

    Args:
        query: Business type to search (e.g., "cafe", "restaurant")
        location: Location string (e.g., "Lagos, Nigeria")
        limit: Max number of places to return

    Returns:
        List of dicts with 'place_id', 'name', 'rating', 'user_ratings_total'.
    """
    if not PLACES_API_KEY:
        print("[Google Places] No GOOGLE_PLACES_API_KEY set. Skipping competitor search.")
        return []

    search_text = f"{query} in {location}" if location else query
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": search_text,
        "key": PLACES_API_KEY,
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()

        if data.get("status") != "OK":
            print(f"[Google Places] Search failed: {data.get('status')}")
            return []

        results = []
        for place in data.get("results", [])[:limit]:
            results.append({
                "place_id": place.get("place_id"),
                "name": place.get("name"),
                "rating": place.get("rating", 0),
                "user_ratings_total": place.get("user_ratings_total", 0),
                "address": place.get("formatted_address", ""),
                "types": place.get("types", []),
            })
        return results

    except Exception as e:
        print(f"[Google Places] Error searching: {e}")
        return []


def fetch_place_reviews(place_id: str) -> list:
    """
    Fetches reviews for a specific place using Google Places Details API.
    Google returns up to 5 most relevant reviews per place.

    Args:
        place_id: The Google Places ID.

    Returns:
        List of review dicts with 'author', 'rating', 'text', 'time'.
    """
    if not PLACES_API_KEY:
        return []

    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "fields": "reviews",
        "key": PLACES_API_KEY,
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        data = resp.json()

        if data.get("status") != "OK":
            print(f"[Google Places] Details failed: {data.get('status')}")
            return []

        reviews = data.get("result", {}).get("reviews", [])
        return [
            {
                "author": r.get("author_name", "Anonymous"),
                "rating": r.get("rating", 3),
                "text": r.get("text", ""),
                "time": r.get("relative_time_description", ""),
            }
            for r in reviews
            if r.get("text")  # Skip empty reviews
        ]

    except Exception as e:
        print(f"[Google Places] Error fetching reviews: {e}")
        return []


def excavate_from_reviews(reviews: list, business_name: str) -> list:
    """
    Takes raw Google reviews and uses LLM to extract behavioral personas.
    Groups reviews by sentiment pattern and generates archetypal personas.

    Args:
        reviews: List of review dicts from fetch_place_reviews.
        business_name: Name of the competitor business.

    Returns:
        List of persona dicts compatible with the Simulator pipeline.
    """
    if not reviews:
        return []

    model_id = os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")

    reviews_text = "\n".join([
        f"- [{r['rating']}/5] {r['text']}"
        for r in reviews
    ])

    prompt = f"""
You are an expert consumer psychologist analyzing real customer reviews for "{business_name}".

Here are the reviews:
{reviews_text}

Based on these REAL reviews, extract distinct customer personas. For each persona:
- "name": A short archetype label
- "narrative": A 100-150 word character portrait based on what the review text reveals about this person's psychology
- "drifts": Any behavioral patterns you can infer (list of strings)
- "avg_rating": Their average rating as a float
- "top_words": 5-8 words that characterize their vocabulary/concerns

Return ONLY a valid JSON array. No markdown, no explanation.
"""

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
            },
        )
        personas = json.loads(response.text)

        normalized = []
        for p in personas:
            normalized.append({
                'name': p.get('name', 'Unknown'),
                'narrative': p.get('narrative', ''),
                'drifts': p.get('drifts', []),
                'avg_rating': float(p.get('avg_rating', 3.5)),
                'top_words': p.get('top_words', []),
                'source': f"Google Reviews - {business_name}",
            })
        return normalized

    except Exception as e:
        print(f"[Google Places] Error excavating personas from reviews: {e}")
        return []


def fetch_competitor_personas(business_category: str, location: str = "", limit: int = 2) -> list:
    """
    Full pipeline: Search competitors -> Fetch their reviews -> Excavate personas.

    Args:
        business_category: Type of business (e.g., "cafe", "restaurant")
        location: Where to search (e.g., "Lagos, Nigeria")
        limit: Number of competitor businesses to analyze

    Returns:
        Flat list of all personas excavated from competitor reviews.
    """
    competitors = search_nearby_competitors(business_category, location, limit)

    if not competitors:
        print("[Google Places] No competitors found. Falling back to synthetic personas.")
        return []

    all_personas = []
    for comp in competitors:
        print(f"[Archaeologist] Excavating reviews from: {comp['name']} ({comp['rating']}★)")
        reviews = fetch_place_reviews(comp["place_id"])
        personas = excavate_from_reviews(reviews, comp["name"])
        all_personas.extend(personas)

    return all_personas


if __name__ == "__main__":
    # Quick test
    results = search_nearby_competitors("cafe", "Lagos, Nigeria", limit=2)
    print(json.dumps(results, indent=2))

    if results:
        reviews = fetch_place_reviews(results[0]["place_id"])
        print(f"\nFetched {len(reviews)} reviews from {results[0]['name']}")
        for r in reviews:
            print(f"  [{r['rating']}/5] {r['text'][:80]}...")
