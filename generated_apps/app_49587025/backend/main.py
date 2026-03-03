from fastapi import FastAPI
from .services import service
app = FastAPI()
@app.get("/items")
def read_items():
    return ["Item1", "Item2"]
@app.post("/items")
def create_item(item: dict):
    print(item)
