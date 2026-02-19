from fastapi import APIRouter
from backend.services.items_service import ItemsService
router = APIRouter()
@router.get("/items")
def read_items():
    return ItemsService().read_items()