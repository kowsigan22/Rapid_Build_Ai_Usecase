from fastapi import FastAPI
from backend.services.main import app as service_app
app = FastAPI()
app.include_router(service_app)
if __name__ == "__main__":
    from uvicorn.main import run
    run("backend:app", host="0.0.0.0", port=8000, reload=True)