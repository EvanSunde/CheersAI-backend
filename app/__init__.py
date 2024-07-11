from fastapi import FastAPI

app = FastAPI()

from app.routes import chat, goals,vapi

app.include_router(chat.router, prefix="/chat")
app.include_router(goals.router, prefix="/goals")
app.include_router(vapi.router, prefix="/vapi")
