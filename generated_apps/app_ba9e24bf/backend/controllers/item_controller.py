from fastapi import APIRouter
from backend.services.item_service import ItemService
router = APIRouter()
service = ItemService()
@router.get("/items")
def get_items():
    return service.get_items()
@router.post("/items")
def create_item(item: dict):
    return service.add_item(item)