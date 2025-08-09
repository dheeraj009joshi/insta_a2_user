import requests

url = "http://20.106.56.49:7000/query/user/a2"  # Flask server URL

payload = {
    "username": "therock",
    "sessions": ["sess1", "sess2", "sess3", "sess4", "sess5"]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
