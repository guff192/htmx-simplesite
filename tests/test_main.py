
from fastapi.testclient import TestClient


def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert 'text/html' in response.headers.get('content-type', '')
    assert ">Simple Site</h1>" in response.text
