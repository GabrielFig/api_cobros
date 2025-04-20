from fastapi import FastAPI
import datetime
from models import Customer

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