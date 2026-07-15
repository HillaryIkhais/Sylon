import asyncio
import os
import sys

sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

# Force Cognee to use Alibaba Qwen by pretending it is OpenAI!
os.environ["LLM_PROVIDER"] = "openai"
os.environ["LLM_MODEL"] = "openai/qwen3-max" 
os.environ["LLM_API_KEY"] = os.getenv("DASHSCOPE_API_KEY", "")
os.environ["OPENAI_API_BASE"] = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
os.environ["COGNEE_SKIP_CONNECTION_TEST"] = "true"

# We also need an embedding model. Alibaba provides text-embedding-v3
os.environ["EMBEDDING_PROVIDER"] = "openai"
os.environ["EMBEDDING_MODEL"] = "openai/text-embedding-v3"

import cognee
from cognee.api.v1.search import SearchType

async def test_cognee():
    print("Testing cognee add and search with Alibaba Qwen natively...")
    text_data = "Sylon Wholesale Perfumes. Business hours are 9-5. We sell Arabian Oud."
    await cognee.add([text_data], dataset_name="test_dataset")
    
    await cognee.cognify()
    
    results = await cognee.search(SearchType.INSIGHTS, query_text="What are the business hours?")
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(test_cognee())
