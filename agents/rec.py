import pandas as pd
import numpy as np
import os
from collections import defaultdict

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
categories_path = os.path.join(DIR, 'data', 'business_categories.csv')
categories = pd.read_csv(categories_path)
_user_names = None

def get_user_name(user_id):
    global _user_names
    if _user_names is None:
            _user_names = pd.read_csv('data/user_names.csv', index_col='user_id')['name'].to_dict()
            return  _user_names.get(user_id, f"User {user_id[:6]}")

def classify_user(rev):
    rev = rev.sort_values('date').reset_index(drop=True)
    
    total_reviews = len(rev)
    avg_rating = rev['stars'].mean()
    avg_useful = rev['useful'].mean()
    first_review = rev['date'].min()
    last_review = rev['date'].max()
    time_span = (last_review - first_review).days / 365
    
    # phase consistency
    third = total_reviews // 3
    early = len(rev.iloc[:third])
    mid = len(rev.iloc[third:2*third])
    recent = len(rev.iloc[2*third:])
    phase_mean = np.mean([early, mid, recent])
    phase_variance = np.std([early, mid, recent]) / phase_mean if phase_mean > 0 else 0
    
    # observer — few reviews, long history, high influence
    if total_reviews <= 8 and time_span >= 3 and avg_useful >= 2:
        return 'observer'
    
    # critical and harsh — low ratings, high useful votes
    if avg_rating <= 2.8 and avg_useful >= 1.5:
        return 'critical'
    
    # off and on — uneven across phases
    if phase_variance > 0.4:
        return 'inconsistent'
    
    # fully committed — consistent, long term
    return 'fully_committed'

def build_segment_report(reviews_df):
   # groups all shortlisted users into behavioral segments and returns a summary of who they are and what they signal for a business.
    users = reviews_df['user_id'].unique()
    
    segments = defaultdict(list)
    
    for uid in users:
        user_df = reviews_df[reviews_df['user_id'] == uid].copy()
        user_df['date'] = pd.to_datetime(user_df['date'])
        segment = classify_user(user_df)
        
        segments[segment].append({
            'user_id': uid,
            'total_reviews': len(user_df),
            'avg_rating': round(user_df['stars'].mean(), 2),
            'avg_useful': round(user_df['useful'].mean(), 2),
            'time_span_years': round(
                (user_df['date'].max() - user_df['date'].min()).days / 365, 1
            ),
            'richness_score': round(user_df['richness_score'].iloc[0], 2)
        })
    
    # build summary
    report = {}
    for segment, users in segments.items():
        avg_rating = np.mean([u['avg_rating'] for u in users])
        avg_useful = np.mean([u['avg_useful'] for u in users])
        avg_span = np.mean([u['time_span_years'] for u in users])
        
        report[segment] = {
            'count': len(users),
            'avg_rating': round(avg_rating, 2),
            'avg_useful_votes': round(avg_useful, 2),
            'avg_years_active': round(avg_span, 1),
            'users': users
        }
    
    return report

def detect_drift_alerts(all_reviews, personas):
    alerts = []
    for user_id, persona in personas.items():
        if 'structured' not in persona:
            continue
            
        phases = persona['structured']['phases']
        early = phases['early']['signal']
        recent = phases['recent']['signal']

        if not early or not recent:
            continue
        
        early_avg = early['avg_rating']
        recent_avg = recent['avg_rating']
        rating_drop = early_avg - recent_avg
        
        # find preferences that persisted into recent phase
        early_words = set(early['top_words'])
        recent_words = set(recent['top_words'])
        persistent_obsessions = early_words & recent_words
        
        # flag if rating dropped significantly
        if rating_drop >= 0.5:
            alerts.append({
                'customer_name': get_user_name(user_id),
                'early_avg': early_avg,
                'recent_avg': recent_avg,
                'rating_drop': round(rating_drop, 2),
                'persistent_obsessions': list(persistent_obsessions)[:5],
                'risk_level': 'high' if rating_drop >= 1.0 else 'medium',
                'signal': f"Rating dropped {round(rating_drop, 2)} stars. Still mentioning: {', '.join(list(persistent_obsessions)[:3])} unmet needs likely."
            })
    
    alerts.sort(key=lambda x: x['rating_drop'], reverse=True)
    return alerts

def find_revenue_opportunities(reviews, personas):
    categories = pd.read_csv('data/business_categories.csv')
    
    print("REVIEWS COLUMNS:" ,reviews.columns.tolist())
    print("CATEGORY COLUMNS:", categories.columns.tolist())
    reviews = reviews.merge(categories[['business_id', 'primary_category']], on='business_id', how='left')
    print("AFTER MERGE:", reviews.columns.tolist())
    for user_id, persona in personas.items():
        if 'structured' not in persona:
            continue
        
    recent = persona['structured']['phases']['recent']['signal']
    early = persona['structured']['phases']['early']['signal']

    opportunities = []
    
    experience_words = {
        'atmosphere', 'ambiance', 'experience', 'kitchen',
        'service', 'quality', 'perfect', 'excellent', 'refined',
        'special', 'memorable', 'exceptional', 'outstanding'
    }
    
    for user_id, persona in personas.items():
        recent = persona['structured']['phases']['recent']['signal']
        early = persona['structured']['phases']['early']['signal']
        
        if not recent or not early:
            continue
        
        # first signal; vocabulary drift toward experience words
        recent_words = set(recent['top_words'])
        early_words = set(early['top_words'])
        experience_overlap = recent_words & experience_words
        early_experience = early_words & experience_words
        experience_growth = len(experience_overlap) - len(early_experience)
        
        # second signal review depth (longer means more emotionally invested)
        user_reviews = reviews[reviews['user_id'] == user_id]
        avg_review_length = user_reviews['text'].apply(lambda x: len(x.split())).mean()
        depth_score = 1 if avg_review_length > 150 else 0
        
        # third signal high useful votes (community validates their judgment)
        avg_useful = user_reviews['useful'].mean()
        influence_score = 1 if avg_useful >= 2 else 0
        
        # fourth signal rating generosity: high but not serial 5 star rater
        rating_quality = 1 if 3.5 <= recent['avg_rating'] <= 4.5 else 0
        
        # fifth signal reviewed same category repeatedly
        category_counts = user_reviews['primary_category'].value_counts()
        loyal_categories = category_counts[category_counts >= 5].index.tolist()
        loyalty_score = len(loyal_categories)
        
        # combined premium score
        premium_score = (
            experience_growth * 2 +
            depth_score * 2 +
            influence_score * 2 +
            rating_quality * 1 +
            loyalty_score * 1
        )
        
        if premium_score >= 4:
            opportunities.append({
                'customer_name': get_user_name(user_id),
                'premium_score': premium_score,
                'recent_avg_rating': recent['avg_rating'],
                'avg_review_length': round(avg_review_length),
                'avg_useful_votes': round(avg_useful, 2),
                'loyal_categories': loyal_categories,
                'experience_signals': list(experience_overlap),
                'opportunity': 'High value experience seeker with strong community influence.',
                'recommended_action': 'Introduce premium offerings, exclusive experiences, or loyalty recognition to convert engagement into higher spend.'
            })
    
    opportunities.sort(key=lambda x: x['premium_score'], reverse=True)
    return opportunities

def describe_segments(report):
    descriptions = {
        'fully_committed': "Your most loyal reviewers. Consistent, long term, and engaged across all phases. These are the customers worth investing in.",
        'inconsistent': "Inconsistent engagers. They show up in bursts then disappear. Usually triggered by strong experiences; good or bad.",
        'critical': "Your harshest judges. Low ratings, high useful votes: meaning people trust their criticism. One bad experience from them is costly.",
        'observer': "Quiet but influential. Rarely review, but when they do, people listen. Their silence is not loyalty, it's patience running out."
    }
    
    output = []
    for segment, data in report.items():
        desc = descriptions.get(segment, '')
        output.append(
            f"\n{segment.upper().replace('_', ' ')} ({data['count']} users)\n"
            f"{desc}\n"
            f"Avg rating: {data['avg_rating']} | "
            f"Avg useful votes: {data['avg_useful_votes']} | "
            f"Avg years active: {data['avg_years_active']}"
        )
    
    return "\n".join(output)


if __name__ == "__main__":
    import json

    all_reviews = pd.read_csv('data/sampled_reviews.csv')
    categories = pd.read_csv('data/business_categories.csv')[['business_id', 'primary_category']]
    all_reviews = all_reviews.merge(categories, on='business_id', how='left')
    all_reviews['date'] = pd.to_datetime(all_reviews['date'])

    print("Building segment report...")
    report = build_segment_report(all_reviews)
    print(describe_segments(report))

    personas = {}
    persona_path = 'outputs/-G7Zkl1wIWBBmD0KRy_sCw_persona.json'
    with open(persona_path) as f:
        raw = json.load(f)
    personas['-G7Zkl1wIWBBmD0KRy_sCw'] = raw

    print("\n DRIFT ALERTS ")
    alerts = detect_drift_alerts(all_reviews, personas)
    for alert in alerts:
        print(f"\nUser: {alert['customer_name']}")
        print(f"Signal: {alert['signal']}")
        print(f"Risk: {alert['risk_level']}")

    print("\n REVENUE OPPORTUNITIES ")
    opportunities = find_revenue_opportunities(all_reviews, personas)
    for opp in opportunities:
        print(f"\nUser: {opp['customer_name']}")
        print(f"Premium score: {opp['premium_score']}")
        print(f"Action: {opp['recommended_action']}")