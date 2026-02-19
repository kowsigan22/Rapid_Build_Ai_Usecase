from fastapi import FastAPI
from backend.controllers.main import app
from backend.services.main import Service
app = FastAPI()
service = Service()
@app.get("/items")
def read_items():
    return service.read_items()
@app.post("/items")
def create_item(item: dict):
    return service.create_item(item)
