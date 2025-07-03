from pydantic import BaseModel
from datetime import datetime

class News(BaseModel):
    title: str
    url: str
    thumbnail_url: str
    date: datetime
    authors: str
    content: str