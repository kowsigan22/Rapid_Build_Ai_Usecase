from backend.db import get_items
from flask import jsonify
def get_all_items():
    return jsonify(get_items())
