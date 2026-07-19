from openserv.server import app
from fastapi.testclient import TestClient

client = TestClient(app)

session_id = "test_demo_123"

# Step 1
print("Step 1")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "start", "mode": "onboarding"})
print(res.json())

# Step 2
print("Step 2")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "Shoe Store", "mode": "onboarding"})
print(res.json())

# Step 3
print("Step 3")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "shoes", "mode": "onboarding"})
print(res.json())

# Step 4
print("Step 4")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "4000 naira", "mode": "onboarding"})
print(res.json())
