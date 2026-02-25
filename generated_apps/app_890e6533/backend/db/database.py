from typing import List
class DB:
    def __init__(self):
        self.items: List[dict] = []
    def read_items(self):
        return self.items
    def create_item(self, item: dict):
        self.items.append(item)
