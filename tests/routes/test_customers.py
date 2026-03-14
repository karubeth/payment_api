from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_customer():

    res = client.post("/customers",json={
        "name":"Alice",
        "email":"alice@example.com"
    })

    assert res.status_code == 201