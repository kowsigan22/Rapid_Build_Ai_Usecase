from fastapi.responses import JSONResponse
from backend.models import Item
class ItemController:
    def __init__(self, service: Service):
        self.service = service

    def read_items(self):
        return self.service.get_items()

    def create_item(self, item: dict):
        return self.service.create_item(item)
