import os
import sys
import asyncio

# Need to insert Cascade directory to sys.path so openserv can be imported
sys.path.insert(0, '/Users/ikhaisoshuare/Cascade')

from dotenv import load_dotenv
load_dotenv('/Users/ikhaisoshuare/Cascade/.env')

from openserv.routers.twilio import process_twilio_message

payload = {
    "From": "whatsapp:+2348157771198",
    "Body": "hi"
}

print("Running process_twilio_message locally to find any silent exceptions...")
try:
    process_twilio_message(payload)
except Exception as e:
    import traceback
    print(f"Exception caught!")
    traceback.print_exc()

print("Finished process_twilio_message.")
