from fastapi import APIRouter, HTTPException, Depends
from app.services.payment_service import PaymentService

router = APIRouter()

def get_service():
    raise NotImplementedError

@router.post("/payments", status_code=201)
def create_payment(body: dict, service: PaymentService = Depends(get_service)):

    customer_id = body.get("customerId")
    amount = body.get("amount")
    currency = body.get("currency")

    if not customer_id or amount is None or not currency:
        raise HTTPException(status_code=400)

    try:
        return service.create_payment(customer_id, amount, currency)
    except Exception:
        raise HTTPException(status_code=400)

@router.post("/payments/{payment_id}/capture")
def capture(payment_id: str, service: PaymentService = Depends(get_service)):
    try:
        return service.capture(payment_id)
    except Exception:
        raise HTTPException(status_code=404)