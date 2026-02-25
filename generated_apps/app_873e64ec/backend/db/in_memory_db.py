class InMemoryDB:
    def __init__(self):
        self.items = []

    def get_all_items(self):
        return self.items

    def create_item(self, item: dict):
        self.items.append(item)
        return len(self.items) - 1
