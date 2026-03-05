from fastapi import FastAPI
from backend.controllers.item_controller import router as item_router

app = FastAPI()

app.include_router(item_router)

@app.get("/")
def root():
    return {"status": "running"}
