from fastapi import APIRouter, HTTPException, Depends
from app.services.payment_service import PaymentService

router = APIRouter()

def get_service():
    raise NotImplementedError

@router.post("/refunds", status_code=201)
def refund(body: dict, service: PaymentService = Depends(get_service)):

    payment_id = body.get("paymentId")
    amount = body.get("amount")

    if not payment_id or amount is None:
        raise HTTPException(status_code=400)

    try:
        return service.refund(payment_id, amount)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))