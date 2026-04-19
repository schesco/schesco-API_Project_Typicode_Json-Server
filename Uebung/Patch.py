import requests

url = "http://localhost:3000/posts/3"

patch_data = {
    "title": "Nur der Titel wurde geändert"
}

response = requests.patch(url, json=patch_data)
print("PATCH Status:", response.status_code)
print("Antwort:", response.json())
