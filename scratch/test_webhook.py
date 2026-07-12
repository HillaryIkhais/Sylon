import asyncio
from openserv.routers.meta import process_whatsapp_message

mock_payload = {
    "messages": [
        {
            "from": "4930577140849",
            "id": "wamid.HBgLNDkzMDU3NzE0MDg0ORUCABEYEjYyQjBEOTk2Nzg0OEIxMzhGMAA=",
            "timestamp": "1691490212",
            "type": "text",
            "text": {
                "body": "Hello, do you have the velvet dress?"
            }
        }
    ],
    "contacts": [
        {
            "profile": {
                "name": "Test User"
            },
            "wa_id": "4930577140849"
        }
    ]
}

print("Running test...")
process_whatsapp_message(mock_payload)
print("Finished!")
