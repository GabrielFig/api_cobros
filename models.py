from pydantic import BaseModel as Base
from uuid import UUID
from datetime import datetime

class BaseModel(Base):
    id: UUID
    create_date: datetime
    update_date: datetime
class Customer(BaseModel):
    name: str
    description: str | None 
    email : str
    age : int