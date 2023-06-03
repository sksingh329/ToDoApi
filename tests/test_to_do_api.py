from fastapi.testclient import TestClient
from main.to_do_api import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/")
    assert response.status_code == 200
    print(response.text)