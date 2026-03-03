from fastapi import FastAPI
from app.routers import colors

app = FastAPI()
app.include_router(colors.router)