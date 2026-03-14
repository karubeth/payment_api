from fastapi import FastAPI
from app.routes import customers, payments, refunds
from app.repos.fake_payment_repo import FakePaymentRepository
from app.services.payment_service import PaymentService

app = FastAPI()

repo = FakePaymentRepository()
service = PaymentService(repo)

def get_service():
    return service

customers.get_service = get_service
payments.get_service = get_service
refunds.get_service = get_service

app.include_router(customers.router)
app.include_router(payments.router)
app.include_router(refunds.router)