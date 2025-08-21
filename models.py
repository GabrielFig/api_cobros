from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field, Relationship

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
    transactions: list["Transaction"] = Relationship(back_populates="customer")


class TransactionBase(SQLModel):
    amount: int
    description: str | None = Field(default=None)


class Transaction(TransactionBase , table=True):
    id: int | None = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="customer.id")
    customer: Customer = Relationship(back_populates="transactions")


class TransactionCreate(TransactionBase):
    customer_id: int = Field(foreign_key="customer.id")
    

class Invoice(BaseModel):
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def total_amount(self) -> int:
        return sum(transaction.amount for transaction in self.transactions)