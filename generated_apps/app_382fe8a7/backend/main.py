from fastapi import FastAPI
from backend.controllers.main import app
app = FastAPI()
app.include_router(app.router)
