import requests
import base64

# Obfuscated sensitive data (API key encoded in Base64)
api_key_encoded = "c2VjcmV0X2tleV9lbmNvZGVkXzEyMzQ1Njc4"
url = "https://example.com/api/data"

# Decoding the Base64 encoded API key
api_key = base64.b64decode(api_key_encoded).decode("utf-8")

# Make API request with sensitive key
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

if response.status_code == 200:
    print("Data fetched  successfully")
else:
    print