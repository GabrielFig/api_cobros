from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field

# class BaseModel(Base):
#     id: int
#     #create_date: datetime
#     #update_date: datetime | None

class CustomerBase(SQLModel):
    name: str = Field(max_length=50)
    description: str | None = Field(default=None)
    email: EmailStr = Field(max_length=50)
    age: int = Field(default=0)


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

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