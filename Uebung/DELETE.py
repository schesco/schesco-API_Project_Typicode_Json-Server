import requests

url = "http://localhost:3000/posts/7"

response = requests.delete(url)
print("DELETE Status:", response.status_code)
