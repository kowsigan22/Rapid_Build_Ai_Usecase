from fastapi import APIRouter
from backend.services import Service
class ItemController:
    def __init__(self, service: Service):
        self.service = service
    def get_router(self):
        router = APIRouter()
        @router.get="/items")
def read_items():
        return self.service.read_items()
        return router