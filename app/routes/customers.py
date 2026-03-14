from fastapi import APIRouter, HTTPException, Depends
from app.services.payment_service import PaymentService

router = APIRouter()

def get_service():
    raise NotImplementedError

@router.post("/customers", status_code=201)
def create_customer(body: dict, service: PaymentService = Depends(get_service)):
    name = body.get("name")
    email = body.get("email")

    if not name:
        raise HTTPException(status_code=400)

    if not email:
        raise HTTPException(status_code=400)

    try:
        return service.create_customer(name, email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))