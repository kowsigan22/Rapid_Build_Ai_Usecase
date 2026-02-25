class InMemoryDatabase:
    def __init__(self):
        self.items = []
    def store_item(self, item):
        self.items.append(item)
    def get_items(self):
        return self.items