# 1_basic_get.py
import requests

# Kostenlose Test-API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(f"Status Code: {response.status_code}")  # 200 = Erfolg
print(f"Response als Text: {response.text[:120]}...")
print(f"Als Python-Dict: {response.json()}")
print(f"Title: {response.json()['userId']}")
print(f"Title: {response.json()['id']}")
print(f"Title: {response.json()['title']}")
print(f"Title: {response.json()['body']}")
