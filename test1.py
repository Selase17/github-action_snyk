import requests

# Hardcoded sensitive data (API Key)
api_key = "1234567890abcdefg"
url = "https://example.com/api/data"

# Make API request with the sensitive key
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})

if response.status_code == 200:
    print("Data fetched successfully!")
else:
    print("Failed to fetch data")
