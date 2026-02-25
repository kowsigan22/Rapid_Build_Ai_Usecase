class InMemoryDatabase:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def add_item(self, item: dict):
        self.items.append(item)
