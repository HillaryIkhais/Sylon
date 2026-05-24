import os
import sys
import pandas as pd
import numpy as np
import json
import math
from tqdm import tqdm
from rouge_score import rouge_scorer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from agents.persona import excavate_user
from agents.llm_client import call_cerebras_json

def generate_synthetic_review(persona_narrative, persona_drifts, business_details):
    drifts_str = "; ".join(persona_drifts) if persona_drifts else "None"

    prompt = f"""
You are a behavioral simulation engine. Based on the psychological persona below, simulate EXACTLY the review this user would write for the following business.
Also, predict the exact star rating (1-5) they would give.

PERSONA NARRATIVE: {persona_narrative}
OBSERVED DRIFTS: {drifts_str}

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
        print(f"Error calling LLM: {e}")
        return {"predicted_stars": 3.0, "synthetic_text": ""}

def evaluate_task_a(num_users=10):
    data_dir = os.path.join(ROOT, 'data')
    train_reviews = pd.read_csv(os.path.join(data_dir, 'train_reviews.csv'))
    test_ground_truth = pd.read_csv(os.path.join(data_dir, 'test_ground_truth.csv'))
    
    business_catalog = pd.read_csv(os.path.join(data_dir, 'business_categories.csv'))
    biz_lookup = business_catalog.set_index('business_id').to_dict('index')

    test_counts = test_ground_truth['user_id'].value_counts()
    eval_users = test_counts.head(num_users).index.tolist()
    
    print(f"\n{'='*60}")
    print(f"  TASK A EVALUATION (RMSE & ROUGE) - {num_users} users")
    print(f"{'='*60}")

    squared_errors = []
    rouge_l_f1_scores = []
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

    for user_id in tqdm(eval_users, desc="Evaluating Users"):
        # Ground truth reviews for this user in the test set
        user_test = test_ground_truth[test_ground_truth['user_id'] == user_id]
        if user_test.empty:
            continue
            
        # Pick one test review to simulate
        test_review = user_test.iloc[0]
        actual_rating = test_review['stars']
        actual_text = str(test_review.get('text', ''))
        business_id = test_review['business_id']
        
        # Excavate Persona using ONLY training data
        persona = excavate_user(user_id, train_reviews)
        if not persona:
            continue
            
        narrative = persona['narrative']
        drifts = persona['structured']['drifts']
        
        # Get business metadata
        biz_info = biz_lookup.get(business_id, {})
        
        # Simulate Review
        simulation = generate_synthetic_review(narrative, drifts, biz_info)
        predicted_stars = float(simulation.get("predicted_stars", 3.0))
        synthetic_text = str(simulation.get("synthetic_text", ""))
        
        # Calculate Squared Error
        sq_err = (predicted_stars - actual_rating) ** 2
        squared_errors.append(sq_err)
        
        # Calculate ROUGE
        if actual_text.strip() and synthetic_text.strip():
            scores = scorer.score(actual_text, synthetic_text)
            rouge_l_f1_scores.append(scores['rougeL'].fmeasure)
        
        print(f"\nUser: {user_id[:8]} | Biz: {biz_info.get('name', 'Unknown')}")
        print(f"Predicted Stars: {predicted_stars} | Actual Stars: {actual_rating}")
        print(f"Synthetic Text: {synthetic_text[:80]}...")
        print(f"Actual Text:    {actual_text[:80]}...")

    if squared_errors:
        rmse = math.sqrt(np.mean(squared_errors))
        avg_rouge_l = np.mean(rouge_l_f1_scores) if rouge_l_f1_scores else 0.0
        
        print(f"\n{'='*60}")
        print(f"  TASK A FINAL RESULTS")
        print(f"  RMSE (Rating Accuracy):  {rmse:.4f}")
        print(f"  ROUGE-L (Text Quality):  {avg_rouge_l:.4f}")
        print(f"{'='*60}")
    else:
        print("No valid evaluation completed.")

if __name__ == '__main__':
    evaluate_task_a(num_users=10)
