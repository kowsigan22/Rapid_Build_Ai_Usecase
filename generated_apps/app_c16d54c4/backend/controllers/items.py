from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from backend.services.items import ItemsService
router = APIRouter()

class Item(BaseModel):
    name: str
    price: int

@router.get('/items')
def get_items():
    return ItemsService().get_all_items()

@router.post('/items')
def create_item(item: Item):
    return ItemsService().create_item(item)
