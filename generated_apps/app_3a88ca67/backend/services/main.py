from backend.db.main import InMemoryDatabase
from fastapi import FastAPI
app = FastAPI()
db = InMemoryDatabase()
@app.get("/items")
def read_items() -> List[Item]:
    return db.get_items()
@app.post("/items")
def create_item(item: Item) -> Item:
    db.add_item(item)
    return item
