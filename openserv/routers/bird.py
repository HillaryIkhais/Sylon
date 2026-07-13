import os
import asyncio
from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhooks/bird", tags=["bird"])

@router.post("/internal/process-bird")
async def receive_bird_internal(request: Request):
    """
    Internal endpoint called by the Next.js API Gateway for Bird (MessageBird) webhooks.
    """
    try:
        body = await request.json()
        print("[Python AI Microservice] Received forwarded webhook from Next.js Gateway (Bird).")
        asyncio.create_task(asyncio.to_thread(process_bird_message, body))
        return {"status": "accepted_for_processing"}
    except Exception as e:
        print(f"[Python AI Error] Error parsing Bird payload: {e}")
        return {"status": "error"}

def process_bird_message(payload: dict):
    """
    Extracts text messages from a Bird webhook and routes them to the Decision Engine.
    """
    from openserv.decision_engine import process_customer_message
    from openserv.persistence import persistence_service
    
    # Bird payload structures can vary, we will try to extract the sender and text safely.
    # Standard Bird WhatsApp payload usually has `message` and `contact` or similar fields.
    try:
        # Try Meta-like structure first (Bird often wraps the Meta payload)
        if "entry" in payload:
            from openserv.routers.meta import process_whatsapp_message
            return process_whatsapp_message(payload)
            
        # Try generic Bird Conversational API structure
        message = payload.get("message", payload)
        text_content = message.get("content", {}).get("text", "")
        if not text_content and "text" in message:
            text_content = message.get("text")
            if isinstance(text_content, dict):
                text_content = text_content.get("body", "")
                
        # Get sender
        sender_id = payload.get("contact", {}).get("msisdn")
        if not sender_id:
            sender_id = message.get("from")
            
        if not sender_id or not text_content:
            print("[Bird Webhook] Could not extract sender or text from payload.")
            print(f"Payload: {payload}")
            return
            
        # Strip '+' from sender_id if present
        if sender_id.startswith("+"):
            sender_id = sender_id[1:]
            
        print(f"[Bird Webhook] Extracted message from {sender_id}: {text_content}")
        
        # Route to primary business (hackathon mode)
        business_id = "demo_business"
        all_businesses = persistence_service.get_all_businesses()
        if all_businesses:
            business_id = all_businesses[0]["business_id"]
            
        process_customer_message(
            text_content=text_content,
            business_id=business_id,
            sender_id=sender_id,
            sender_name="Customer",
            channel="bird"
        )
        
    except Exception as e:
        print(f"[Bird Webhook] Error processing message: {e}")
