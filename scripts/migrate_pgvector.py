import os
import sys
import psycopg2

sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

# Supabase direct connection for migrations (session mode port 5432)
# We must use the direct URL for CREATE EXTENSION
password = os.getenv("SUPABASE_PASSWORD", "b3aSI47LZJZZPgj")
direct_url = os.getenv("DIRECT_URL")
if "[YOUR-PASSWORD]" in direct_url:
    direct_url = direct_url.replace("[YOUR-PASSWORD]", password)

def run_migration():
    print("Connecting to Supabase to initialize pgvector...")
    conn = psycopg2.connect(direct_url)
    conn.autocommit = True
    cursor = conn.cursor()
    
    print("Enabling vector extension...")
    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    
    print("Creating business_knowledge_vectors table...")
    # Alibaba text-embedding-v3 outputs 1024 dimensions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS business_knowledge_vectors (
            id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
            business_id VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            metadata JSONB,
            embedding vector(1024),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        );
    """)
    
    print("Creating vector index for fast similarity search...")
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_business_knowledge_embedding 
        ON business_knowledge_vectors 
        USING hnsw (embedding vector_cosine_ops);
    """)
    
    print("Creating business_id index for fast filtering...")
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_business_knowledge_business_id 
        ON business_knowledge_vectors(business_id);
    """)
    
    print("Migration complete!")
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_migration()
