from typing import List, Dict
class InMemoryDatabase:
    def __init__(self):
        self.items: List[Dict] = []

    def get_items(self) -> List[Dict]:
        return self.items

    def add_item(self, item: Dict):