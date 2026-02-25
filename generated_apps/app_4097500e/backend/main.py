from fastapi import FastAPI
from backend.controllers import ItemController
app = FastAPI()
@app.get("/items")
def read_items():
    return [Item(name="item1", description="desc1"), Item(name="item2", description="desc2")]