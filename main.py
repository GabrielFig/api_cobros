from fastapi import FastAPI
import datetime
from models import Customer, Transaction, Invoice

app = FastAPI()



@app.get("/")
async def root ():
    return {"message": "Hello World"}

@app.get("/time")
async def get_time():
    return {"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  

@app.post("/customers")
async def create_customer(customer: Customer):
    return {"customer": customer} 

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return {"transaction": transaction}

@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return {"invoice": invoice}