import os
import sys
import json

sys.path.insert(0, "/Users/ikhaisoshuare/Cascade")
from dotenv import load_dotenv
load_dotenv("/Users/ikhaisoshuare/Cascade/.env")

from openserv.persistence import persistence_service
from openserv.decision_engine import build_context, analyze_intent_and_risk

business_id = "demo_business"
sender_id = "2348157771198"
message = "Hi, do you deliver to Abuja? How much is the shipping fee?"

print("Building context...")
context = build_context(business_id, sender_id)
print("Context:")
print(context)

print("\nCalling analyze_intent_and_risk...")
try:
    result = analyze_intent_and_risk(message, context)
    print("Result:")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"Exception: {e}")
