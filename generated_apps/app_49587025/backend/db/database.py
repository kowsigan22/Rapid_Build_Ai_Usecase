class Database:
    def __init__(self):
        self.items = [Item(name="Item1"), Item(name="Item2"]]
    def get_all_items(self):
        return self.items
    def save_item(self, item: dict):
        self.items.append(Item(**item))
