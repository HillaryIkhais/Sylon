import sys
import os
sys.path.insert(0, os.path.abspath("."))
from openserv.orchestrator import evaluate_route
import asyncio

async def test():
    res = await asyncio.to_thread(evaluate_route, "Diesel costs spiked 20% overnight. Compare raising prices 15% vs closing 2 hours earlier vs reducing menu size.", [])
    print(res)

asyncio.run(test())
