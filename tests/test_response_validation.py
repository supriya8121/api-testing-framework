import requests

def test_validate_post_response():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data
