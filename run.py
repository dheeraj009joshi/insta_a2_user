import requests

url = "http://56.228.26.41:7000/query/user/a2"  

payload = {
    "username": "therock",
    "sessions": [
    "72834751862%3A8Iod3xoTDGeHnE%3A0%3AAYddVMv0sxQgcXigTPcR6Ambp1DkiYT236Id7A02Gw","72834751862%3A8Iod3xoTDGeHnE%3A0%3AAYddVMv0sxQgcXigTPcR6Ambp1DkiYT236Id7A02Gw",
    "72834751862%3A8Iod3xoTDGeHnE%3A0%3AAYddVMv0sxQgcXigTPcR6Ambp1DkiYT236Id7A02Gw","72834751862%3A8Iod3xoTDGeHnE%3A0%3AAYddVMv0sxQgcXigTPcR6Ambp1DkiYT236Id7A02Gw","72834751862%3A8Iod3xoTDGeHnE%3A0%3AAYddVMv0sxQgcXigTPcR6Ambp1DkiYT236Id7A02Gw"]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
