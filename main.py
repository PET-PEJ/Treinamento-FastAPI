from fastapi import FastAPI
from api.api_v1.router import router
from database.database import init_db

init_db()

app = FastAPI()

app.include_router(router, prefix="/api/v1")