from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_refund():

    customer = client.post("/customers",json={
        "name":"Alice",
        "email":"alice2@example.com"
    }).json()

    payment = client.post("/payments",json={
        "customerId":customer["id"],
        "amount":1000,
        "currency":"usd"
    }).json()

    client.post(f"/payments/{payment['id']}/capture")

    res = client.post("/refunds",json={
        "paymentId":payment["id"],
        "amount":1000
    })

    assert res.status_code == 201