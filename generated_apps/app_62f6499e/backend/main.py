from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.controllers.item_controller import router as item_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(item_router)

@app.get("/")
def root():
    return {"status": "running"}
