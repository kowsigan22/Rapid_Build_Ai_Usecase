from fastapi import FastAPI
from pydantic import BaseModel
from backend.services.service import Service
app = FastAPI()
@app.get("/items")
def read_items():
    return [Service(item) for item in items]
@app.post("/items")
def create_item(request: dict):
    items.append(Service(request))
    return Service(request)
items = []

if __name__ == "__main__":
    from uvicorn.main import run
    run(app, host="0.0.0.0", port=8000,
        log_level="info")