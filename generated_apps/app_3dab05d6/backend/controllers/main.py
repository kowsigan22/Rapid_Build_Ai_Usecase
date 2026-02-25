from fastapi import FastAPI
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    return [item]
@app.post("/items")
def create_item(item: dict):
    return item
