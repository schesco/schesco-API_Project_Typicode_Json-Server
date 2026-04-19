# 2_query_params.py
import requests

# Suche Posts von User 1
url = "http://localhost:3000/posts"

params = {
    "userId": 4,
#   "_limit": 2 # Nur 3 Ergebnisse
}

response = requests.get(url, params=params)
print("Status:", response.status_code)
print(f"URL mit Parametern: {response.url}")
#post=response.json()
if len(response.json()) > 1:
    for post in response.json():
        print(f"Post {post['id']}: {post['title'][:50]}")
#print(f'Post {response['id']}: {response['title'][:50]}')
#print(f"Post {post['id']}: {post['title'][:50]}")