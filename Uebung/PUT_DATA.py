import requests

url = "http://localhost:3000/posts"

response = requests.get(url)
print("GET Status:", response.status_code)
print("Antwort:", response.json())
url = "http://localhost:3000/posts/1"
put_data = {
    "title": "Komplett ersetzt",
    "body": "Neuer Body",
    "userId": 1
}

response = requests.put(url, json=put_data)
print("PUT Status:", response.status_code)
print("Antwort:", response.json())