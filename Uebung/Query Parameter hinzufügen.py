# 2_query_params.py
import requests

# Suche Posts von User 1
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
    "_limit": 3  # Nur 3 Ergebnisse
}

response = requests.get(url, params=params)

print(f"URL mit Parametern: {response.url}")
for post in response.json():
    print(f"Post {post['id']}: {post['title'][:50]}")