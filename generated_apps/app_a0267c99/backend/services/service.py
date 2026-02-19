from backend.db.db import InMemoryDatabase
class Service:
    def __init__(self):
        self.db = InMemoryDatabase()
    def get_all_items(self) -> List[Dict]:
        return self.db.get_all_items()
    def create_item(self, item: Dict):
        self.db.create_item(item)
