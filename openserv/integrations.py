import os
import requests
import json

def send_meta_message(platform: str, to_number: str, message_text: str, business_id: str = None) -> dict:
    """
    Sends an outgoing message via the Meta Graph API (WhatsApp, Instagram, Facebook).
    Supports multi-tenancy by fetching the business's specific Meta tokens from the database.
    """
    access_token = None
    phone_id = None
    
    if business_id:
        from openserv.persistence import persistence_service
        tokens = persistence_service.get_business_meta_tokens(business_id)
        if tokens:
            access_token = tokens["meta_access_token"]
            phone_id = tokens["whatsapp_phone_id"]
            
    # Fallback to env vars if DB doesn't have it (for backward compatibility during migration)
    if not access_token:
        access_token = os.environ.get("META_ACCESS_TOKEN")
    if not phone_id:
        phone_id = os.environ.get("WHATSAPP_PHONE_NUMBER_ID")
        
    if not access_token or not phone_id:
        raise Exception(f"Missing OAuth credentials for business_id: {business_id}. Cannot send WhatsApp message.")
        
    d360_key = os.environ.get("D360_API_KEY")
    
    if d360_key and platform.lower() == "whatsapp":
        # Using Sandbox environment for Hackathon demo
        url = "https://waba-sandbox.360dialog.io/v1/messages"
        headers = {
            "D360-API-KEY": d360_key,
            "Content-Type": "application/json"
        }
    else:
        api_version = "v25.0"
        url = f"https://graph.facebook.com/{api_version}/{phone_id}/messages"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": platform.lower(),
            "recipient_type": "individual",
            "to": to_number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message_text
            }
        }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending Meta message: {e}")
        return {"error": str(e), "status": "failed"}


def reply_to_google_review(review_name: str, reply_text: str) -> dict:
    """
    Replies to a specific Google Review using the Google Business Profile API.
    review_name format: accounts/{accountId}/locations/{locationId}/reviews/{reviewId}
    """
    # Assuming OAuth token is acquired and stored in env for hackathon demo
    access_token = os.environ.get("GOOGLE_BUSINESS_TOKEN", "mock_google_token")
    
    url = f"https://mybusiness.googleapis.com/v4/{review_name}/reply"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "comment": reply_text
    }

    try:
        response = requests.put(url, headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error replying to Google review: {e}")
        return {"error": str(e), "status": "failed"}
def send_twilio_message(to_number: str, message_text: str) -> dict:
    """
    Sends an outgoing WhatsApp message using the Twilio REST API.
    Used as the sandbox for Hackathon testing without Meta verification.
    """
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("TWILIO_PHONE_NUMBER", "+14155238886")
    
    if not account_sid or not auth_token:
        raise Exception("Missing TWILIO_ACCOUNT_SID or TWILIO_AUTH_TOKEN. Cannot send Twilio message.")
        
    if not to_number.startswith("whatsapp:"):
        if not to_number.startswith("+"):
            to_number = f"+{to_number}"
        to_number = f"whatsapp:{to_number}"
        
    if not from_number.startswith("whatsapp:"):
        from_number = f"whatsapp:{from_number}"
        
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"
    
    data = {
        "To": to_number,
        "From": from_number,
        "Body": message_text
    }
    
    try:
        response = requests.post(url, data=data, auth=(account_sid, auth_token))
        response.raise_for_status()
        print(f"[Twilio Integration] Successfully sent message to {to_number}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[Twilio Integration Error] Failed to send message: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return {"error": str(e)}
