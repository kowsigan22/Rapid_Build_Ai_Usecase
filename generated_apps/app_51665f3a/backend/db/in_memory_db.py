class InMemoryDB:
    def __init__(self):
        self.items = []

    def get_all(self):
        return self.items

    def add(self, item):
        self.items.append(item)
        return item


db_instance = InMemoryDB()
