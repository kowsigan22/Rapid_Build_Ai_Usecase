from uvicorn.main import run
from backend.app import app
run(app, host="0.0.0.0", port=8000)