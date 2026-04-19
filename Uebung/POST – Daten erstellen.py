# 3_post_request.py
import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "userId": 2,
    "title": "Mein erster API-Post",
    "body": "Das ist der Inhalt",

}

response = requests.post(url, json=new_post)  # json= wandelt automatisch

print(f"Status: {response.status_code}")  # 201 = Created
print(f"Antwort: {response.json()}")
print(f"Server gab ID: {response.json()['id']}")  # 101 (fiktiv)