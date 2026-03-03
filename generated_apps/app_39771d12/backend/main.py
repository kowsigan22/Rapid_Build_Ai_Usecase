from fastapi import FastAPI
from backend.controllers import ItemController
from backend.services import Service
from backend.db import Database

app = FastAPI()
controller = ItemController(app)
app.include_router(controller.router)

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)