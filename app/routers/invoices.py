from fastapi import APIRouter
from models import Invoice

router = APIRouter()

@router.post("/invoices")
async def create_invoice(invoice: Invoice):
    return {"invoice": invoice}