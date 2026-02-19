from fastapi import FastAPI
from pydantic import BaseModel
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    return [Service().get_all_items()]
@app.post("/items")
def create_item(item: dict):
    item_service = Service()
    item_service.create_item(item)
    return item
