import os
import json
import logging
from openserv.persistence import persistence_service

logger = logging.getLogger('morlen.embedding_engine')

def generate_embedding(text: str):
    """
    Calls Google Gemini API to embed a piece of text via REST.
    Uses model gemini-embedding-2 scaled down to 768 dims to support pgvector HNSW limits.
    """
    import requests
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        logger.error("GEMINI_API_KEY not found!")
        return None
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-embedding-2:embedContent?key={gemini_key}"
        resp = requests.post(url, json={
            "model": "models/gemini-embedding-2",
            "content": {
                "parts": [{"text": text}]
            },
            "outputDimensionality": 768
        })
        if resp.status_code == 200:
            return resp.json()['embedding']['values']
        else:
            logger.error(f"Gemini API Error: {resp.text}")
            return None
    except Exception as e:
        logger.error(f"Embedding error: {e}")
        return None

def ingest_knowledge(business_id: str, content: str, metadata: dict = None):
    """
    Ingests text into the Supabase pgvector table.
    """
    embedding = generate_embedding(content)
    if not embedding:
        return False
        
    meta_json = json.dumps(metadata) if metadata else "{}"
    
    # Format the vector as a string for Postgres: '[0.1, 0.2, ...]'
    embedding_str = f"[{','.join(map(str, embedding))}]"
    
    try:
        with persistence_service.get_connection() as conn:
            query = """
                INSERT INTO business_knowledge_vectors (business_id, content, metadata, embedding)
                VALUES (?, ?, ?, ?)
            """
            conn.execute(query, (business_id, content, meta_json, embedding_str))
        return True
    except Exception as e:
        logger.error(f"DB Insert error: {e}")
        return False

def search_knowledge(business_id: str, query_text: str, limit: int = 3):
    """
    Performs cosine similarity search against pgvector.
    """
    query_embedding = generate_embedding(query_text)
    if not query_embedding:
        return []
        
    embedding_str = f"[{','.join(map(str, query_embedding))}]"
    
    try:
        with persistence_service.get_connection() as conn:
            # <=> is cosine distance. 1 - (A <=> B) gives cosine similarity.
            query = """
                SELECT content, metadata, 1 - (embedding <=> ?::vector) as similarity
                FROM business_knowledge_vectors
                WHERE business_id = ?
                ORDER BY embedding <=> ?::vector
                LIMIT ?
            """
            cursor = conn.execute(query, (embedding_str, business_id, embedding_str, limit))
            results = cursor.fetchall()
            return [dict(r) for r in results]
    except Exception as e:
        logger.error(f"Vector search error: {e}")
        return []
