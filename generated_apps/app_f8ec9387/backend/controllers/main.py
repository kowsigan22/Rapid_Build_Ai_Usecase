from fastapi import FastAPI
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    return Service().get_all_items()
@app.post("/items")
def create_item(item: dict):
    Service().create_item(item)
