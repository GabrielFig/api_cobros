import datetime

from fastapi import FastAPI
from models import Customer, CustomerCreate, Invoice, Transaction
from postgres import SessionDep, init_db
from sqlmodel import select

app = FastAPI(lifespan=init_db)



@app.get("/")
async def root ():
    return {"message": "Hello World"}

@app.get("/time")
async def get_time():
    return {"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  

db_customers: list[Customer] = []

@app.post("/customers", response_model=Customer)
async def create_customer(customer: CustomerCreate, sesion: SessionDep):
    customer = Customer.model_validate(customer.model_dump())
    sesion.add(customer)
    sesion.commit()
    sesion.refresh(customer)
    return customer

@app.get("/customers", response_model=list[Customer])
async def list_customers(session: SessionDep):
    return session.exec(select(Customer)).all() 

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return {"transaction": transaction}

@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return {"invoice": invoice}