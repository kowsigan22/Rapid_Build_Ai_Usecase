from fastapi import APIRouter
from backend.services import ItemService
router = APIRouter()
@router.get("/items")
def read_items():
    return ItemService().read_items()
@router.post("/items")
def create_item(item: dict):
    return ItemService().create_item(item)
