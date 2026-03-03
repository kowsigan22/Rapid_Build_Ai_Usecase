from backend.db import Database

class Service:
    def __init__(self):
        pass

    def get_items(self):
        db = Database()
        return db.get_all_items()
