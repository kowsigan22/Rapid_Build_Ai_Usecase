from backend.db import DB
class Service:
    def __init__(self, db: DB):
        self.db = db

    def get_items(self):
        return [Item(name="Item 1", description="Description 1"), Item(name="Item 2", description="Description 2"]

    def create_item(self, item: dict):
        items = [Item(name=item["name"], description=item["description"])]
        return items
