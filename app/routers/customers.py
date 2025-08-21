from typing import List
from sqlmodel import select
from fastapi import HTTPException, APIRouter, status, Depends

from models import Customer, CustomerCreate
from postgres import SessionDep

router = APIRouter()

@router.post(
    "/customers",
    response_model=Customer,
    tags=["customers"],
    status_code=status.HTTP_201_CREATED
)
async def create_customer(
    customer_data: CustomerCreate,
    session: SessionDep
):
    """Create a new customer."""
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get(
    "/customers",
    response_model=List[Customer],
    tags=["customers"]
)
async def list_customers(session: SessionDep):
    """List all customers."""
    return session.exec(select(Customer)).all()

@router.get(
    "/customers/{customer_id}",
    response_model=Customer,
    tags=["customers"]
)
async def get_customer(customer_id: int, session: SessionDep):
    """Get a customer by ID."""
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put(
    "/customers/{customer_id}",
    response_model=Customer,
    tags=["customers"]
)
async def update_customer(
    customer_id: int,
    customer_data: CustomerCreate,
    session: SessionDep
):
    """Update a customer completely."""
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer_data.model_dump().items():
        setattr(customer, key, value)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.delete(
    "/customers/{customer_id}",
    tags=["customers"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_customer(customer_id: int, session: SessionDep):
    """Delete a customer."""
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    session.delete(customer)
    session.commit()
    return

@router.patch(
    "/customers/{customer_id}",
    response_model=Customer,
    tags=["customers"]
)
async def patch_customer(
    customer_id: int,
    customer_data: CustomerCreate,
    session: SessionDep
):
    """Partially update a customer."""
    customer = session.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    for key, value in customer_data.model_dump(exclude_unset=True).items():
        setattr(customer, key, value)
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer
