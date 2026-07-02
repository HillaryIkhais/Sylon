import os
import requests
import json

def send_meta_message(platform: str, to_number: str, message_text: str) -> dict:
    """
    Sends an outgoing message via the Meta Graph API (WhatsApp, Instagram, Facebook).
    """
    # Fallback to demo defaults if env vars are missing
    access_token = os.environ.get("META_ACCESS_TOKEN", "mock_access_token")
    phone_id = os.environ.get("WHATSAPP_PHONE_NUMBER_ID", "mock_phone_id")
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
