from client import JsonServerClient

def main():
    client = JsonServerClient("http://localhost:3000/posts")

    print("\n--- Alle Posts abrufen ---")
    print(client.get_all())

    print("\n--- Neuen Post erstellen ---")
    new_post = client.create({
        "title": "Neuer Post",
        "body": "Das wird gespeichert!",
        "userId": 2
    })
    print(new_post)

    print("\n--- Einzelnen Post abrufen ---")
    print(client.get_one(new_post["id"]))

    print("\n--- Post komplett ersetzen (PUT) ---")
    updated = client.update_full(new_post["id"], {
        "title": "Komplett ersetzt",
        "body": "Neuer Body",
        "userId": 2
    })
    print(updated)

    print("\n--- Post teilweise ändern (PATCH) ---")
    patched = client.update_partial(new_post["id"], {
        "title": "Nur der Titel geändert"
    })
    print(patched)

    print("\n--- Post löschen ---")
    print(client.delete(new_post["id"]))

if __name__ == "__main__":
    main()
