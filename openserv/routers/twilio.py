import asyncio
from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhooks/twilio", tags=["twilio"])

@router.post("/internal/process-twilio")
async def receive_twilio_internal(request: Request):
    """
    Internal endpoint called by the Next.js API Gateway for Twilio webhooks.
    """
    try:
        body = await request.json()
        print("[Python AI Microservice] Received forwarded webhook from Next.js Gateway (Twilio).")
        asyncio.create_task(asyncio.to_thread(process_twilio_message, body))
        return {"status": "accepted_for_processing"}
    except Exception as e:
        print(f"[Python AI Error] Error parsing Twilio payload: {e}")
        return {"status": "error"}

def process_twilio_message(payload: dict):
    """
    Extracts text messages from a Twilio webhook and routes them to the Decision Engine.
    """
    from openserv.decision_engine import process_customer_message
    from openserv.persistence import persistence_service
    
    try:
        # Twilio sends Form Data which Next.js converts to JSON keys: From, Body
        sender_id = payload.get("From", "")
        text_content = payload.get("Body", "")
        
        if not sender_id or not text_content:
            print("[Twilio Webhook] Could not extract sender or text from payload.")
            return
            
        # Twilio WhatsApp numbers prefix with "whatsapp:"
        if sender_id.startswith("whatsapp:"):
            sender_id = sender_id.replace("whatsapp:", "")
        if sender_id.startswith("+"):
            sender_id = sender_id[1:]
            
        print(f"[Twilio Webhook] Extracted message from {sender_id}: {text_content}")
        
        # Route to primary business (hackathon mode)
        business_id = "demo_business"
        all_businesses = persistence_service.get_all_businesses()
        if all_businesses:
            business_id = all_businesses[0]["business_id"]
            
        process_customer_message(
            text_content=text_content,
            business_id=business_id,
            sender_id=sender_id,
            sender_name="Twilio User",
            channel="twilio"
        )
        
    except Exception as e:
        print(f"[Twilio Webhook] Error processing message: {e}")
