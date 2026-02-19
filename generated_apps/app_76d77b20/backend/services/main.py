from fastapi import FastAPI
from backend.db.main import Database
app = FastAPI()
db = Database()

@app.get("/items")
def read_items():
    return db.get_items()

@app.post("/items")
def create_item(item: Item):
    db.create_item(item)
