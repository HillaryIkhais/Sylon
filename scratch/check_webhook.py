import requests

# Try combinations of the ambiguous characters in the API key
base_key = "JX89UP09C9MIC59PWRCSVAF7U8OH8UIR"

variations = [
    "JX89UP09C9MIC59PWRCSVAF7U8OH8UIR", # All uppercase
    "JX89UP09C9MlC59PWRCSVAF7U8OH8UlR", # lowercase L instead of I
    "JX89UPO9C9MIC59PWRCSVAF7U8OH8UIR", # letter O instead of 0
    "JX89UP09C9MIC59PWRCSVAF7U80H8UIR", # zero instead of O
]

for key in variations:
    try:
        response = requests.get(
            "https://waba-sandbox.360dialog.io/v1/configs/webhook",
            headers={"D360-API-KEY": key, "Content-Type": "application/json"}
        )
        if response.status_code == 200:
            print(f"SUCCESS with key: {key}")
            print(f"Registered Webhook URL: {response.json()}")
            break
        else:
            print(f"Failed with key {key}: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
