from db.main import InMemoryDatabase
class Service:
    def __init__(self):
        self.db = InMemoryDatabase()
    def get_items(self) -> List[Dict]:
        return self.db.get_items()
    def add_item(self, item: Dict) -> None:
        self.db.add_item(item)
