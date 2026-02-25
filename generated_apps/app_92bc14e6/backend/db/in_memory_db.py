class InMemoryDB:
    items = []

    def get_items(self):
        return self.items

    def add_item(self, item):
        self.items.append(item)
