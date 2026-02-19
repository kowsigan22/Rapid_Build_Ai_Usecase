from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str

@app.get("/items")
def read_items():
    return [Item(id=1, name="Item 1", description="Description 1"), Item(id=2, name="Item 2", description="Description 2")]

@app.post("/items")
def create_item(item: Item):
    return item
