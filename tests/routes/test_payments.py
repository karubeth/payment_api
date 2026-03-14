from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_payment():

    customer = client.post("/customers",json={
        "name":"Bob",
        "email":"bob@example.com"
    }).json()

    res = client.post("/payments",json={
        "customerId":customer["id"],
        "amount":1000,
        "currency":"usd"
    })

    assert res.status_code == 201