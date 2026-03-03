from fastapi import FastAPI
from backend.controllers import ItemController
from backend.services import Service
app = FastAPI()
controller = ItemController(app)
app.include_router(controller.router)
