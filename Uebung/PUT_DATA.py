import requests

url = "http://localhost:3000/posts"

response = requests.get(url)
print("GET Status:", response.status_code)
print("Antwort:", response.json())
url = "http://localhost:3000/posts/1"
put_data = {
    "userId": 1,
    "title": "Komplett ersetzt",
    "body": "Neuer Body"

}

response = requests.put(url, json=put_data)
print("PUT Status:", response.status_code)
print("Antwort:", response.json())