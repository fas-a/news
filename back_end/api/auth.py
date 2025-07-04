from fastapi import APIRouter, HTTPException, Request, Depends
from configuration import db, secret_key
from db.models.auth import LoginRequest
from bcrypt import checkpw
import jwt
from datetime import datetime, timedelta

router = APIRouter()

collection = db["users"]

def verify_token(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="No token provided")
    token = auth.split(" ")[1]
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/login")
async def login(data: LoginRequest):
    account = collection.find_one({"username": data.username})
    if not account:
        raise HTTPException(status_code=401, detail="User not found")
    password_valid = checkpw(
        data.password.encode('utf-8'),
        account['password'].encode('utf-8')
    )
    if password_valid:
        expire = datetime.utcnow() + timedelta(hours=1)
        token = jwt.encode(
            {"username": data.username, "exp": expire},
            secret_key,
            algorithm="HS256"
        )
        return {"message": "Login successful", "token": token}
    else:
        raise HTTPException(status_code=401, detail="Invalid password")

@router.get("/validate")
async def validate_token(payload: dict = Depends(verify_token)):
    return {"valid": True, "user": payload}
