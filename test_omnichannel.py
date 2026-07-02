import os
import sys

# Ensure backend imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from openserv.integrations import send_meta_message, reply_to_google_review

def simulate_agent_execution():
    print("==================================================")
    print(" Sylon OS: Omnichannel Execution Layer Simulation")
    print("==================================================\n")
    
    print("[1/4] Orchestrator Agent received incoming WhatsApp webhook.")
    print("[2/4] Sales and Inventory Agents debating response...")
    print("[3/4] Action Planner reached consensus.\n")
    
    print("--- EXECUTING META GRAPH API (WHATSAPP) ---")
    customer_phone = "+2348000000000"
    whatsapp_reply = "Hi Mary! Yes, we have exactly 3 pairs of the red Nikes left in size 42. Because you're one of our best customers, I've applied a 50% discount to your delivery. Should I pack it up for you?"
    
    result = send_meta_message("whatsapp", customer_phone, whatsapp_reply)
    print(f"Meta API Response: {result}\n")
    
    print("--- EXECUTING GOOGLE BUSINESS API (REVIEWS) ---")
    review_id = "accounts/123/locations/456/reviews/789"
    google_reply = "Thank you so much for the 5-star review! We're glad you enjoyed the vibe, and we'll keep the generator noise down next time. See you soon!"
    
    result2 = reply_to_google_review(review_id, google_reply)
    print(f"Google API Response: {result2}\n")
    
    print("==================================================")
    print(" ✅ Execution Complete. Sylon OS is Omnichannel.")
    print("==================================================")

if __name__ == "__main__":
    simulate_agent_execution()
