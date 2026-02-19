from fastapi import FastAPI
from backend.db.main import DB
app = FastAPI()
db = DB()

@app.get("/items")
def read_items():
    return db.get_items()

@app.post("/items")
def create_item(item: Item):
    return db.add_item(item)
