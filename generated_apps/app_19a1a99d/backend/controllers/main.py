from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.get("/items")
def read_items():
    return [Item(name="item 1", description="description 1"), Item(name="item 2", description="description 2")]