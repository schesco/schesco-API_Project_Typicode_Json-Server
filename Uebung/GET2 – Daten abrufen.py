import requests

url = "http://localhost:3000/posts"

response = requests.get(url)
print("Status:", response.status_code)
print("Daten:", response.json())