import asyncio
import os
import sys

sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

# Use gemini natively since Cognee supports it!
os.environ["LLM_PROVIDER"] = "gemini"
os.environ["LLM_MODEL"] = "gemini/gemini-2.0-flash" 
# or maybe just "gemini-2.0-flash" if Cognee handles the prefix
os.environ["LLM_API_KEY"] = os.getenv("GEMINI_API_KEY", "")

# We also need an embedding model.
os.environ["EMBEDDING_PROVIDER"] = "gemini"
os.environ["EMBEDDING_MODEL"] = "models/text-embedding-004"

import cognee
from cognee.api.v1.search import SearchType

async def test_cognee():
    print("Testing cognee add and search with Gemini natively...")
    text_data = "Sylon Wholesale Perfumes. Business hours are 9-5. We sell Arabian Oud."
    await cognee.add([text_data], dataset_name="test_dataset")
    
    await cognee.cognify()
    
    results = await cognee.search(SearchType.INSIGHTS, query_text="What are the business hours?")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(test_cognee())
