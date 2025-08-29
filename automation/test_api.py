import requests

def test_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

def test_json_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert "userId" in data
    assert data["id"] == 1
