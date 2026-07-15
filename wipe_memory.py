import sys
import os
sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

from openserv.persistence import persistence_service

print("Wiping AI memory to clear the confused context...")
with persistence_service.get_connection() as conn:
    conn.execute("DELETE FROM business_memories WHERE business_id = 'demo_business';")
    print(f"Deleted all previous memories for demo_business.")
