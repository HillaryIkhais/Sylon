import requests

url = "https://morlen.onrender.com/webhooks/twilio/internal/process-twilio"
data = {
    "From": "whatsapp:+16824429239",
    "To": "whatsapp:+14155238886",
    "Body": "hello test"
}

print(f"Testing live URL: {url}")
try:
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except Exception as e:
    print(f"Error: {e}")
