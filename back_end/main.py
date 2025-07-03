from fastapi import FastAPI
from api.news import router as news_router

app = FastAPI()
app.include_router(news_router)