import os
import time
import uuid
from typing import Dict, Any, List
from fastapi import APIRouter, Request, HTTPException, Response, BackgroundTasks
from openserv.persistence import persistence_service
from openserv.orchestrator import process_user_scenario
from openserv.tools import tool_send_meta_message

router = APIRouter(prefix="/webhooks/meta", tags=["meta"])

META_VERIFY_TOKEN = os.environ.get("META_VERIFY_TOKEN")

@router.post("/internal/process-whatsapp")
async def receive_whatsapp_internal(request: Request):
    """
    Internal endpoint called by the Next.js API Gateway.
    Next.js has already verified the Meta signature and returned a 200 OK.
    """
    try:
        body = await request.json()
        print("[Python AI Microservice] Received forwarded webhook from Next.js Gateway.")
        
        obj_type = body.get("object")
        import asyncio
        
        # Handle Meta-wrapped payloads
        if obj_type in ["whatsapp_business_account", "instagram", "page"]:
            for entry in body.get("entry", []):
                if obj_type == "whatsapp_business_account":
                    asyncio.create_task(asyncio.to_thread(process_whatsapp_message, entry))
        
        # Handle 360dialog direct unwrapped payloads
        elif "messages" in body or ("changes" in body and isinstance(body["changes"], list)):
            print("[Python AI] Detected 360dialog direct payload.")
            asyncio.create_task(asyncio.to_thread(process_whatsapp_message, body))
        else:
            # Maybe it's wrapped in an array?
            if isinstance(body, list) and len(body) > 0 and "messages" in body[0]:
                asyncio.create_task(asyncio.to_thread(process_whatsapp_message, body[0]))
                    
        return {"status": "accepted_for_processing"}
    except Exception as e:
        print(f"[Python AI Error] Error parsing internal payload: {e}")
        return {"status": "error"}


def process_whatsapp_message(entry: dict):
    """
    Extracts text messages from a WhatsApp webhook entry and routes them to the Decision Engine.
    """
    from openserv.decision_engine import process_customer_message
    from openserv.persistence import persistence_service
    import time
    import uuid

    # Normalize payload structure (Meta vs 360dialog)
    changes = entry.get("changes", [])
    if not changes and ("messages" in entry or "contacts" in entry):
        # It's a 360dialog direct payload, mock the 'change' structure
        changes = [{"value": entry}]

    for change in changes:
        value = change.get("value", {})
        messages = value.get("messages", [])
        contacts = value.get("contacts", [])
        
        metadata = value.get("metadata", {})
        phone_number_id = metadata.get("phone_number_id", "unknown_360_number")
        
        # Multi-Tenant Routing
        business_id = persistence_service.get_business_by_phone_id(phone_number_id)
        
        if not business_id:
            # HACKATHON DEMO BYPASS: If unregistered, just use the first business in the DB
            print(f"[Webhook Routing] Unregistered phone {phone_number_id}. Defaulting to primary business.")
            all_businesses = persistence_service.get_all_businesses()
            if all_businesses:
                business_id = all_businesses[0]["business_id"]
            else:
                print("[Webhook Dropped] No businesses registered in the database.")
                return

        contact_map = {c.get("wa_id"): c.get("profile", {}).get("name", "Unknown") for c in contacts}
        owner_phone = persistence_service.get_owner_phone(business_id)

        for msg in messages:
            if msg.get("type") == "text":
                sender_id = msg.get("from")
                sender_name = contact_map.get(sender_id, "Unknown")
                text_content = msg.get("text", {}).get("body", "")
                
                # Check if this message is from the Business Owner
                if owner_phone and sender_id == owner_phone:
                    from openserv.decision_engine import handle_owner_message
                    try:
                        handle_owner_message(business_id, text_content)
                    except Exception as ai_e:
                        print(f"[Business Intent Router Error] Pipeline failed: {ai_e}")
                    return # Stop execution so we don't process it as a customer message
                
                # 1. Log the incoming message to Business Memory
                memory_id = f"wm_{uuid.uuid4().hex[:12]}"
                created_at = str(int(time.time())) 
                try:
                    with persistence_service.get_connection() as conn:
                        formatted_content = f"[{sender_name} via WhatsApp]: {text_content}"
                        conn.execute("""
                            INSERT INTO business_memories 
                            (memory_id, business_id, source, text_content, created_at)
                            VALUES (?, ?, ?, ?, ?)
                        """, (memory_id, business_id, "whatsapp_inbound", formatted_content, created_at))
                except Exception as e:
                    print(f"[Morlen Meta Ingest Error] Failed to store memory: {e}")

                # 2. Pipe it into the new Customer Decision Engine
                try:
                    process_customer_message(text_content, business_id, sender_id, sender_name)
                except Exception as ai_e:
                    print(f"[Decision Engine Error] Pipeline failed: {ai_e}")
