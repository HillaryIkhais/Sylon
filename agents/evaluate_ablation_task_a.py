import os
import sys
import pandas as pd
import numpy as np
import json
import math
from tqdm import tqdm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from agents.persona import excavate_user
from agents.llm_client import call_cerebras_json

def generate_synthetic_review(persona_narrative, business_details):
    # ABLATION: NO DRIFTS PASSED.
    prompt = f"""
You are a behavioral simulation engine. Based on the psychological persona below, simulate EXACTLY the review this user would write for the following business.
Also, predict the exact star rating (1-5) they would give.

PERSONA NARRATIVE: {persona_narrative}
OBSERVED DRIFTS: None

BUSINESS DETAILS:
Name: {business_details.get('name', 'Unknown')}
Categories: {business_details.get('categories', 'Unknown')}
Average Rating: {business_details.get('stars', 'Unknown')} ({business_details.get('review_count', 'Unknown')} reviews)

Output ONLY a JSON object in this exact format:
{{
    "predicted_stars": 4.0,
    "synthetic_text": "I really enjoyed the ambiance here..."
}}
"""
    try:
        response = call_cerebras_json(prompt, temperature=0.3, max_tokens=1500)
        return response
    except Exception as e:
        return {"predicted_stars": 3.0, "synthetic_text": ""}

def run_ablation():
    data_dir = os.path.join(ROOT, 'data')
    train_reviews = pd.read_csv(os.path.join(data_dir, 'train_reviews.csv'))
    test_ground_truth = pd.read_csv(os.path.join(data_dir, 'test_ground_truth.csv'))
    business_catalog = pd.read_csv(os.path.join(data_dir, 'business_categories.csv'))
    biz_lookup = business_catalog.set_index('business_id').to_dict('index')

    test_counts = test_ground_truth['user_id'].value_counts()
    eval_users = test_counts.head(10).index.tolist()
    
    squared_errors = []

    for user_id in tqdm(eval_users, desc="Ablation"):
        user_test = test_ground_truth[test_ground_truth['user_id'] == user_id]
        if user_test.empty: continue
            
        test_review = user_test.iloc[0]
        actual_rating = test_review['stars']
        business_id = test_review['business_id']
        
        persona = excavate_user(user_id, train_reviews)
        if not persona: continue
            
        narrative = persona['narrative']
        biz_info = biz_lookup.get(business_id, {})
        
        simulation = generate_synthetic_review(narrative, biz_info)
        predicted_stars = float(simulation.get("predicted_stars", 3.0))
        
        sq_err = (predicted_stars - actual_rating) ** 2
        squared_errors.append(sq_err)

    if squared_errors:
        rmse = math.sqrt(np.mean(squared_errors))
        print(f"\nABLATION RMSE (No Drift): {rmse:.4f}")

if __name__ == '__main__':
    run_ablation()
