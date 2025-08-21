from fastapi import APIRouter, HTTPException, status
from models import Transaction, TransactionCreate
from postgres import SessionDep
from sqlmodel import select

router = APIRouter()

@router.post("/transactions", tags=["transactions"], status_code=status.HTTP_201_CREATED)
async def create_transaction(transaction: TransactionCreate, session: SessionDep):
    transaction_data = transaction.model_dump()
    customer = session.get(Transaction, transaction_data.get("customer_id"))
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer not found"
        )
    transaction_db = Transaction.model_validate(transaction_data)
    session.add(transaction_db)
    session.commit()
    session.refresh(transaction_db)
    return transaction_db

@router.get("/transactions", tags=["transactions"])
async def list_transactions(session: SessionDep):
    query = select(Transaction)
    transactions = session.exec(query).all()
    return transactions
