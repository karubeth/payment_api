from app.services.payment_service import PaymentService
from app.repos.fake_payment_repo import FakePaymentRepository

def test_create_customer_success():

    repo = FakePaymentRepository()
    service = PaymentService(repo)

    customer = service.create_customer("Alice","alice@example.com")

    assert customer["name"] == "Alice"

def test_create_payment_pending():

    repo = FakePaymentRepository()
    service = PaymentService(repo)

    c = service.create_customer("Bob","bob@example.com")

    payment = service.create_payment(c["id"],1000,"usd")

    assert payment["status"] == "pending"