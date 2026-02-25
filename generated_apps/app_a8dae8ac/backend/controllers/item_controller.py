from fastapi import APIRouter
from backend.services.item_service import ItemService
router = APIRouter()
@router.get("/items")
def read_items():
    return [Item(name="Item 1"), Item(name="Item 2")]