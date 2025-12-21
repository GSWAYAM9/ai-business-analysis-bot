from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router as api_router
from utils.logger import setup_logger

setup_logger()

app = FastAPI(title="AI Business Analysis Bot - Backend", version="0.1")

# CORS FIX (prevents 405 errors)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "AI Business Analysis Bot (backend) is running. Use /api/analyze"}
