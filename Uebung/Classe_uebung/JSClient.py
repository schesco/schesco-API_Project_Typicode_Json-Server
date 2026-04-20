import requests
from sniffio import current_async_library
from urllib3 import request


class Client:

    def __init__(self,URL):
        self.URL=URL

    def data_get(self):
        response=requests.get(self.URL)
        return response.status_code,response.json()

    def data_posts(self):
        posts_number=0
        post_limits=4
        status_code=[]
        posts_elements=[]
        while posts_number < post_limits:

            new_post = {
                "userId": int(input("User ID: ")),
                "title": input("Titel: "),
                "body": input("Body: ")
            }
            response = requests.post(self.URL, json=new_post)
            status_code.append(response.status_code)
            posts_elements.append(response.json())
            posts_number=posts_number + 1

        return status_code,posts_elements


    def data_query(self):
        params = {
            "userId": 4
            #   "_limit": 2 # Nur 3 Ergebnisse
        }
        response = requests.get(self.URL, params=params)

        return response.status_code ,response.json()

    def data_put(self, ID:str):

        put_data = {
            "userId": 1,
            "title": "Komplett ersetzt",
            "body": "Neuer Body"
        }
        response = requests.put(self.URL +'/'+ ID, json=put_data)
        return response.status_code ,response.json()

    def data_patch(self,ID:str ):
        patch_data={
            "title": "Komplett ersetzt blablaba"
        }
        response = requests.put(self.URL + '/' + ID, json=patch_data)
        return response.status_code, response.json()

    def data_delete(self,ID:str):

        response=requests.delete(self.URL+'/'+ID)
        return response.status_code, response.json()


url="http://localhost:3000/posts"
obj_client=Client(url)

_,elements=obj_client.data_posts()

print(elements)