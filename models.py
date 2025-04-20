from pydantic import BaseModel as Base
from pydantic import EmailStr
from datetime import datetime

class BaseModel(Base):
    id: int
    create_date: datetime
    #update_date: datetime | None

class Customer(BaseModel):
    name: str
    description: str | None 
    email : EmailStr
    age : int

class Transaction(BaseModel):
    amount: int
    description: str | None

class Invoice(BaseModel):
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def total_amount(self) -> int:
        return sum(transaction.amount for transaction in self.transactions)