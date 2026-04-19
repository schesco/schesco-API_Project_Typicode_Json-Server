import requests

url = "http://localhost:3000/posts"

posts = [
    {
        "userId": 3,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum"
    },
    {
        "userId": 4,
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque"
    }
]

for p in posts:
    response = requests.post(url, json=p)
    print("Status:", response.status_code, "→", response.json())

new_post = {
    "title": "Mein erster echter Post",
    "body": "Das wird gespeichert!",
    "userId": 5
}

response = requests.post(url, json=new_post)
print("Status:", response.status_code)
print("Antwort:", response.json())