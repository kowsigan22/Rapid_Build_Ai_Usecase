from fastapi import FastAPI
from backend.controllers.main import app
from backend.services.main import Service

app = app
service = Service()

@app.get("/items")
def read_items():
    return service.get_items()

@app.post("/items")
def add_item(item: dict):
    service.add_item(item)
    return item