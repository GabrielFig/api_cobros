from fastapi import FastAPI
import datetime
from models import Customer, Transaction, Invoice, CustomerCreate

app = FastAPI()



@app.get("/")
async def root ():
    return {"message": "Hello World"}

@app.get("/time")
async def get_time():
    return {"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  

db_customers: list[Customer] = []

@app.post("/customers", response_model=Customer)
async def create_customer(customer: CustomerCreate):
    customer = Customer.model_validate(customer.model_dump())

    customer.id = len(db_customers) + 1
    db_customers.append(customer)
    return customer

@app.get("/customers", response_model=list[Customer])
async def list_customers():
    return db_customers 

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return {"transaction": transaction}

@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return {"invoice": invoice}