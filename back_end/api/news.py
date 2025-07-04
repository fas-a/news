from fastapi import APIRouter, HTTPException, Query
from configuration import db
from db.schemas.news import news_list, individual_news
from db.models.news import News
from bson import ObjectId

router = APIRouter()

collection = db["news"]

@router.get("/news")
async def get_all_news(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    data = collection.find().skip(skip).limit(limit)
    return news_list(data)

@router.post("/news")
async def create_news(news_item : News):
    try:
        response = collection.insert_one(dict(news_item))
        return {"status_code":200, "id":str(response.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error ocured {e}")

@router.get("/news/count")
async def get_news_count():
    return {"count": collection.count_documents({})}
    
@router.get("/news/{news_id}")
async def get_news_by_id(news_id: str):
    id = ObjectId(news_id)
    data = collection.find_one({"_id":id})
    if not data:
        raise HTTPException(status_code=404, detail="News not found")
    return individual_news(data)

@router.put("/news/{news_id}")
async def update_news(news_id:str, updated_news:News):
    try:
        id = ObjectId(news_id)
        data = collection.find_one({"_id":id})
        if not data:
            return HTTPException(status_code=404, detail=f"News does not exits")
        response = collection.update_one({"_id":id}, {"$set": dict(updated_news)})
        return {"status_code":200, "message": "News Updated Successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")

@router.delete("/news/{news_id}")
async def delete_news(news_id:str):
    try:
        id = ObjectId(news_id)
        data = collection.find_one({"_id":id})
        if not data:
            return HTTPException(status_code=404, detail=f"News does not exits")
        response = collection.delete_one({"_id":id})
        return {"status_code":200, "message": "News Deleted Successfully"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured {e}")
    