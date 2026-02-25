from backend.db.in_memory_db import InMemoryDB
class Service:
    def __init__(self):
        self.db = InMemoryDB()
    def get_all_items(self) -> List[Dict]:
        return self.db.get_all_items()
    def create_item(self, item: Dict) -> Dict:
        return self.db.create_item(item)