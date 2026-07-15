import sys
import os

sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

from openserv.embedding_engine import ingest_knowledge, search_knowledge

def test_vectors():
    print("Ingesting business policies...")
    ingest_knowledge(
        business_id="demo_business",
        content="Our standard shipping fee to Abuja is 5000 NGN. Delivery takes 2-3 business days.",
        metadata={"type": "policy", "category": "shipping"}
    )
    ingest_knowledge(
        business_id="demo_business",
        content="We sell wholesale perfumes including Arabian Oud and Baccarat Rouge. Minimum order is 300,000 NGN.",
        metadata={"type": "policy", "category": "products"}
    )
    
    print("Ingestion complete. Running vector search...")
    results = search_knowledge(
        business_id="demo_business", 
        query_text="How much does it cost to deliver to Abuja?",
        limit=2
    )
    
    print("\n--- Search Results ---")
    for r in results:
        print(f"Similarity: {r['similarity']:.4f}")
        print(f"Content: {r['content']}")
        print(f"Metadata: {r['metadata']}")
        print("----------------------")

if __name__ == "__main__":
    test_vectors()
