from backend.controllers.main import app
if __name__ == "__main__":
    from uvicorn.main import run
    run("backend:app", host="0.0.0.0", port=8000)
