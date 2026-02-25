from fastapi import FastAPI
from backend.controllers.main import app
from backend.db.main import Database
from typing import List, Dict

class Service:
    def __init__(self, db: Database):