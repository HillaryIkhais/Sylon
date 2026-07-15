import asyncio
import os
import sys

sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

import cognee
from cognee.api.v1.search import SearchType

async def test_cognee():
    print("Testing cognee add and search...")
    # Add a document
    text_data = "Sylon Wholesale Perfumes. Business hours are 9-5. We sell Arabian Oud."
    await cognee.add([text_data], dataset_name="test_dataset")
    
    # Cognify (Embed and Build Graph)
    await cognee.cognify()
    
    # Search
    results = await cognee.search(SearchType.INSIGHTS, query_text="What are the business hours?")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(test_cognee())
