from typing import List

class Database:
    def __init__(self):
        self.items: List[str] = []

    def get_all_items(self):
        return self.items

    def store(self, item_name: str):
        self.items.append(item_name)
