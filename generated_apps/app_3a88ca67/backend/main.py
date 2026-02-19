from fastapi import FastAPI
from backend.controllers.main import app as controllers_app
app = FastAPI()
app.include_router(controllers_app)
if __name__ == "__main__":
    from uvicorn.main import run
    run("backend:app", reload=True, port=8000)