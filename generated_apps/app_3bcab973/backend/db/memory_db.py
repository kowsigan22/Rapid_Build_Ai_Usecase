from typing import List
class MemoryDB:
    items: List[dict] = []
    def get_items(self) -> List[dict]:
        return self.items
    def store_item(self, item: dict):
        self.items.append(item)
