from typing import List
class DB:
    def __init__(self):
        self.items: List[Item] = []

    def get_items(self):
        return self.items

    def create_item(self, item: dict):
        self.items.append(Item(name=item["name"], description=item["description"]))
