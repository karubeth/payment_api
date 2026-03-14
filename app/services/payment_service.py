from app.utils.validators import validate_amount, validate_currency, validate_email, generate_id

class PaymentService:

    STATUS_PENDING = "pending"
    STATUS_SUCCEEDED = "succeeded"
    STATUS_FAILED = "failed"

    def __init__(self, repo):
        self.repo = repo

    def create_customer(self, name, email):
        if not name or not name.strip():
            raise Exception("Name is required")

        if not validate_email(email):
            raise Exception("Invalid email")

        if self.repo.find_customer_by_email(email):
            raise Exception("Email already exists")

        customer = {
            "id": generate_id("cus"),
            "name": name,
            "email": email
        }

        return self.repo.save_customer(customer)

    def create_payment(self, customer_id, amount, currency):

        if not self.repo.find_customer_by_id(customer_id):
            raise Exception("Customer not found")

        if not validate_amount(amount):
            raise Exception("Invalid amount")

        if not validate_currency(currency):
            raise Exception("Invalid currency")

        payment = {
            "id": generate_id("pay"),
            "customerId": customer_id,
            "amount": amount,
            "currency": currency,
            "status": self.STATUS_PENDING
        }

        return self.repo.save_payment(payment)

    def capture(self, payment_id):

        payment = self.repo.find_payment_by_id(payment_id)

        if not payment:
            raise Exception("Payment not found")

        if payment["status"] != self.STATUS_PENDING:
            raise Exception("Cannot capture")

        payment["status"] = self.STATUS_SUCCEEDED
        return self.repo.save_payment(payment)

    def fail(self, payment_id):

        payment = self.repo.find_payment_by_id(payment_id)

        if not payment:
            raise Exception("Payment not found")

        if payment["status"] != self.STATUS_PENDING:
            raise Exception("Cannot fail")

        payment["status"] = self.STATUS_FAILED
        return self.repo.save_payment(payment)

    def refund(self, payment_id, amount):

        payment = self.repo.find_payment_by_id(payment_id)

        if not payment:
            raise Exception("Payment not found")

        if payment["status"] != self.STATUS_SUCCEEDED:
            raise Exception("Cannot refund")

        if not validate_amount(amount):
            raise Exception("Invalid amount")

        refunds = self.repo.find_refunds_by_payment(payment_id)
        refunded_total = sum(r["amount"] for r in refunds)

        if refunded_total + amount > payment["amount"]:
            raise Exception("Refund exceeds payment amount")

        refund = {
            "id": generate_id("ref"),
            "paymentId": payment_id,
            "amount": amount,
            "status": "succeeded"
        }

        return self.repo.save_refund(refund)

    def get_payment(self, id):
        return self.repo.find_payment_by_id(id)

    def get_customer(self, id):
        return self.repo.find_customer_by_id(id)

    def get_payments_for_customer(self, customer_id):
        return self.repo.find_payments_by_customer(customer_id)