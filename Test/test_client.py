import pytest
from client import JsonServerClient

BASE_URL = "http://localhost:3000/posts"

@pytest.fixture
def client():
    return JsonServerClient(BASE_URL)

def test_create_post(client):
    post = client.create({
        "title": "Test",
        "body": "Test Body",
        "userId": 1
    })
    assert "id" in post
    assert post["title"] == "Test"

def test_get_one(client):
    post = client.create({
        "title": "Eintrag",
        "body": "Body",
        "userId": 1
    })
    fetched = client.get_one(post["id"])
    assert fetched["id"] == post["id"]

def test_update_full(client):
    post = client.create({
        "title": "Alt",
        "body": "Alt",
        "userId": 1
    })
    updated = client.update_full(post["id"], {
        "title": "Neu",
        "body": "Neu",
        "userId": 1
    })
    assert updated["title"] == "Neu"

def test_delete(client):
    post = client.create({
        "title": "Delete",
        "body": "Delete",
        "userId": 1
    })
    result = client.delete(post["id"])
    assert result["deleted"] == post["id"]
