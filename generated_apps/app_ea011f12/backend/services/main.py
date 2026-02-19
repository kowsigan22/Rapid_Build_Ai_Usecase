from backend.db.main import InMemoryDatabase
class ItemService:
    def __init__(self, db: InMemoryDatabase):
        self.db = db
    def get_items(self) -> List[Dict]:
        return self.db.get_items()
    def create_item(self, item: Dict) -> Dict:
        self.db.store_item(item)
        return item
