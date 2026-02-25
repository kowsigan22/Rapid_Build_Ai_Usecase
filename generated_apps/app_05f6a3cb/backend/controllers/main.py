from fastapi import FastAPI
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    service = Service()
    return service.read_all_items()
@app.post("/items")
def create_item(item: dict):
    service = Service()
    return service.create_item(item)
