from typing import List, Dict
class InMemoryDatabase:
    def __init__(self):
        self.items = []
    def get_all_items(self) -> List[Dict]:
        return self.items
    def create_item(self, item: Dict) -> Dict:
        self.items.append(item)
        return item