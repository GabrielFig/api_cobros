import datetime

from fastapi import FastAPI
from models import Invoice, Transaction
from postgres import init_db
from app.routers import customers, transactions

app = FastAPI(lifespan=init_db)
app.include_router(customers.router)
app.include_router(transactions.router)



@app.get("/")
async def root ():
    return {"message": "Hello World"}

@app.get("/time")
async def get_time():
    return {"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  

@app.post("/transactions")
async def create_transaction(transaction: Transaction):
    return {"transaction": transaction}

@app.post("/invoices")
async def create_invoice(invoice: Invoice):
    return {"invoice": invoice}