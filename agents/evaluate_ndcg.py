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
from agents.rec import classify_user

def dcg_at_k(r, k):
    #Discounted cumulative gain (dcg)
    r = np.asfarray(r)[:k]
    if r.size:
        return np.sum(np.subtract(np.power(2, r), 1) / np.log2(np.arange(2, r.size + 2)))
    return 0.

def ndcg_at_k(r, k):
    #Normalized discounted cumulative gain (ndcg)
    ideal_r = sorted(r, reverse=True)
    idcg = dcg_at_k(ideal_r, k)
    if not idcg:
        return 0.
    return dcg_at_k(r, k) / idcg

def hit_rate_at_k(recommended_ids, truth_ids, k):
    top_k = recommended_ids[:k]
    hits = set(top_k).intersection(set(truth_ids))
    return 1 if len(hits) > 0 else 0

def rank_candidates_with_llm(persona_narrative, persona_drifts, candidates):
    business_descriptions = ""
    for i, b in enumerate(candidates):
        business_descriptions += f"\n[{i}] ID: {b['business_id']} | Name: {b['name']} | Categories: {b.get('categories', '')} | Rating: {b.get('stars', 0)} ({b.get('review_count', 0)} reviews)"

    drifts_str = "; ".join(persona_drifts) if persona_drifts else "None"

    prompt = f"""
You are a highly analytical behavioral matching engine. 
Rank the following businesses based on how perfectly they fit this customer persona.

PERSONA NARRATIVE: {persona_narrative}
OBSERVED DRIFTS: {drifts_str}

CANDIDATE BUSINESSES:{business_descriptions}

For each business ID, assign a match_score from 0 to 100 based on how well the business categories and vibe align with the persona's preferences and dealbreakers.
Return ONLY a JSON object mapping the exact business_id to its score and a 1-sentence reason.
Example format:
{{
    "business_id_1": {{"score": 85, "reason": "Fits their need for quiet ambiance."}},
    "business_id_2": {{"score": 30, "reason": "Too loud, violates their main dealbreaker."}}
}}
"""
    try:
        response = call_cerebras_json(prompt, temperature=0.3, max_tokens=2000)
        return response
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return {b['business_id']: {"score": np.random.randint(0, 100), "reason": "error fallback"} for b in candidates}

def evaluate_ndcg(num_users=5):
    data_dir = os.path.join(ROOT, 'data')
    train_df = pd.read_csv(os.path.join(data_dir, 'train_reviews.csv'))
    test_df = pd.read_csv(os.path.join(data_dir, 'test_ground_truth.csv'))
    
    business_df = pd.read_csv(os.path.join(data_dir, 'business_categories.csv'))
    
    # Get top users with most test reviews
    test_counts = test_df['user_id'].value_counts()
    eval_users = test_counts.head(num_users).index.tolist()
    
    print(f"Evaluating {num_users} users for NDCG@10...")
    
    ndcg_scores = []
    hit_rates = []
    
    for user_id in eval_users:
        print(f"\n--- Evaluating User: {user_id} ---")
        
        # 1. Get ground truth positives (businesses they visited and rated >= 4 in test set)
        user_test = test_df[(test_df['user_id'] == user_id)]
        positives = user_test[user_test['stars'] >= 4]['business_id'].tolist()
        
        if not positives:
            print("No highly-rated ground truth positives in test set. Skipping.")
            continue
            
        print(f"Ground truth positives: {len(positives)}")
        
        # 2. Build Persona from Train Set
        print("Excavating persona from train set...")
        persona = excavate_user(user_id, train_df)
        if not persona:
            print("Failed to excavate persona. Skipping.")
            continue
            
        narrative = persona['narrative']
        drifts = persona['structured']['drifts']
        
        # 3. Construct Candidate Pool (Positives + Random Negatives)
        np.random.shuffle(positives)
        target_positives = positives[:3]
        
        positive_businesses = business_df[business_df['business_id'].isin(target_positives)].to_dict('records')
        
        num_negatives = 15 - len(positive_businesses)
        negatives = business_df[~business_df['business_id'].isin(positives)].sample(n=num_negatives).to_dict('records')
        
        candidates = positive_businesses + negatives
        np.random.shuffle(candidates)
        

        # 4. LLM Ranking
        print(f"Ranking {len(candidates)} candidates using Cerebras Qwen 235B...")
        llm_scores = rank_candidates_with_llm(narrative, drifts, candidates)
        
        # 5. Extract and sort scores
        ranked_list = []
        for c in candidates:
            bid = c['business_id']
            score_data = llm_scores.get(bid, {"score": 0})
            # Handle if LLM returned an int instead of dict
            if isinstance(score_data, int) or isinstance(score_data, float):
                 score = float(score_data)
            else:
                 score = float(score_data.get('score', 0))
                 
            ranked_list.append((bid, score))
            
        ranked_list.sort(key=lambda x: x[1], reverse=True)
        recommended_ids = [x[0] for x in ranked_list]
        
        # 6. Calculate Metrics
        # r is a list of relevance scores (1 if in positives, 0 otherwise) for the ranked items
        r = [1 if bid in positives else 0 for bid in recommended_ids]
        
        n_score = ndcg_at_k(r, 10)
        h_score = hit_rate_at_k(recommended_ids, positives, 10)
        
        print(f"NDCG@10: {n_score:.4f}")
        print(f"HitRate@10: {h_score:.4f}")
        
        ndcg_scores.append(n_score)
        hit_rates.append(h_score)
        
    if ndcg_scores:
        print("\n" + "="*40)
        print("FINAL EVALUATION METRICS")
        print(f"Average NDCG@10:  {np.mean(ndcg_scores):.4f}")
        print(f"Average HitRate@10: {np.mean(hit_rates):.4f}")
        print("="*40)
    else:
        print("\nNo valid users evaluated.")

if __name__ == '__main__':
    # Run a small 3-user test by default
    evaluate_ndcg(num_users=3)
