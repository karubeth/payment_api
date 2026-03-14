class FakePaymentRepository:

    def __init__(self):
        self.customers = {}
        self.payments = {}
        self.refunds = {}

    def save_customer(self, customer):
        self.customers[customer["id"]] = customer
        return customer

    def find_customer_by_id(self, id):
        return self.customers.get(id)

    def find_customer_by_email(self, email):
        for c in self.customers.values():
            if c["email"] == email:
                return c
        return None

    def save_payment(self, payment):
        self.payments[payment["id"]] = payment
        return payment

    def find_payment_by_id(self, id):
        return self.payments.get(id)

    def find_payments_by_customer(self, customer_id):
        return [p for p in self.payments.values() if p["customerId"] == customer_id]

    def save_refund(self, refund):
        self.refunds[refund["id"]] = refund
        return refund

    def find_refunds_by_payment(self, payment_id):
        return [r for r in self.refunds.values() if r["paymentId"] == payment_id]

    def clear(self):
        self.customers.clear()
        self.payments.clear()
        self.refunds.clear()