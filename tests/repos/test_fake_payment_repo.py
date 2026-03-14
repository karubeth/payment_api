from app.repos.fake_payment_repo import FakePaymentRepository

def test_save_and_find_customer():
    repo = FakePaymentRepository()

    customer = {"id":"cus_1","name":"Alice","email":"alice@test.com"}
    repo.save_customer(customer)

    result = repo.find_customer_by_id("cus_1")

    assert result == customer

def test_clear_repo():
    repo = FakePaymentRepository()

    repo.save_customer({"id":"1","name":"a","email":"a"})
    repo.clear()

    assert repo.find_customer_by_id("1") is None