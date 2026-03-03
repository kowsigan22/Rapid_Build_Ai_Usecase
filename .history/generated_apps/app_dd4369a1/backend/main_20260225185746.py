from fastapi import FastAPI
from backend.controllers import ItemController
from backend.models import 
app = FastAPI()
@app.get("/items")
def read_items():
    return [Item(name="Item 1"), Item(name="Item 2")]