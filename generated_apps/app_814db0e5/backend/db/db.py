from typing import List, Dict
class Database:
    items: List[Dict] = [{"name": "Item 1", "description": "Description 1"}, {"name": "Item 2", "description": "Description 2"}]
    def get_items(self) -> List[Dict]:
        return self.items
    def store_item(self, item: Dict):
        self.items.append(item)
