import os

from dotenv import load_dotenv
from fastapi import FastAPI

from src.api import auth

load_dotenv()

app = FastAPI()

from src.api import user
from src.database import create_db_and_tables

create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])


@app.get("/health")
async def health_check():
    return {"status": "ok"}
