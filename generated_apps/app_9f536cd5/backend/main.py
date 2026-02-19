from fastapi import FastAPI
from backend.services.service import Service
app = FastAPI()

service = Service()
@app.get("/items")
def read_items():
    return service.get_items()

@app.post("/items")
def create_item(item: dict) -> None:
    service.add_item(item)
