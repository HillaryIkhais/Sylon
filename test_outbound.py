import os
import requests
from dotenv import load_dotenv

load_dotenv()

def force_test_message():
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_PHONE_NUMBER", "+14155238886")
    
    # The user's WhatsApp number that successfully joined the sandbox
    to_number = "whatsapp:+2348157771198"
    from_number = f"whatsapp:{from_number.replace('whatsapp:', '')}"
        
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
    
    data = {
        "To": to_number,
        "From": from_number,
        "Body": "🚀 Morlen Backend Override: I am officially connected to your phone! The outbound API is working perfectly."
    }
    
    print(f"Sending test message from {from_number} to {to_number}...")
    try:
        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        response.raise_for_status()
        print(f"Success! Response: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Details: {e.response.text}")

if __name__ == "__main__":
    force_test_message()
