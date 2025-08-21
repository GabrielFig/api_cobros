from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class CustomerBase(SQLModel):
    name: str = Field(max_length=50)
    description: str | None = Field(default=None)
    email: EmailStr = Field(max_length=50)
    age: int = Field(default=0)


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
