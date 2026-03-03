from fastapi import FastAPI
from backend.controllers.items import ItemsController
app = FastAPI()
app.include_router(ItemsController.router)
