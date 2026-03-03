from typing import List

class DB:
    def __init__(self):
        self.items = []

    def get_items(self) -> List[Item]:
        return self.items

    def add_item(self, item: Item):
        self.items.append(item)
