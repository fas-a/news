from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.news import router as news_router
from api.auth import router as auth_router
from configuration import cors

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[cors],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(news_router)
app.include_router(auth_router)