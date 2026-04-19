import requests

url = "http://localhost:3000/posts"

response1=requests.get(url)
print("Status:", response1.status_code)
print("Antwort:", response1.json())

new_post = {
    "userId": 2,
    "title": "Mein erster echter Post",
    "body": "Das wird gespeichert!",
}

response2 = requests.post(url, json=new_post)
print("Status:", response2.status_code)
print("Antwort:", response2.json())