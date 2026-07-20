from openserv.server import app
from fastapi.testclient import TestClient

client = TestClient(app)

session_id = "test_demo_new_123"

# Step 1
print("Step 1 (start)")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "start", "mode": "onboarding"})
print(res.json())

# Step 2
print("Step 2 (hello)")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "hello", "mode": "onboarding"})
print(res.json())

# Step 3
print("Step 3 (fashion apparel)")
res = client.post("/demo/chat", json={"session_id": session_id, "text": "fashion apparel", "mode": "onboarding"})
print(res.json())
