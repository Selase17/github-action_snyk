import requests
import base64

# Obfuscated sensitive data (API Key)
api_key_encoded = "MTIzNDU2Nzg5MGFiY2RlZmdo"  # Base64 encoded API key
url = "https://example.com/api/data"

# Decode the API key
api_key = base64.b64decode(api_key_encoded).decode('utf-8')

# Make API request with the sensitive key
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

if response.status_code == 200:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data")
