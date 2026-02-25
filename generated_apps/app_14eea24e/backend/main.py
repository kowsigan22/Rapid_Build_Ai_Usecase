from fastapi import FastAPI
from backend.controllers.main import app
app = app
if __name__ == "__main__":
    from uvicorn.main import run
    run("main:app", host="0.0.0.0", port=8000)
