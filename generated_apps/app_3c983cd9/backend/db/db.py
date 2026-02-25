from typing import List
class DB:
    def __init__(self):
        self.items = []

    def get_all_items(self) -> List[dict]:
        return self.items

    def create_item(self, item: dict):
        self.items.append(item)
