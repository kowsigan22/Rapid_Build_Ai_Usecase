from uvicorn.main import run
from backend.service import Service
if __name__ == "__main__":
    service = Service()
    run("uvicorn main:app --host 0.0.0.0 --port 8000", access_log=False)