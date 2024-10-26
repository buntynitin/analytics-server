from fastapi import FastAPI, HTTPException, Request
from pymongo import MongoClient
import os

app = FastAPI()

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["your_database_name"]
collection = db["analytics"]

@app.post("/")
async def analytics(request: Request):
    try:
        body = await request.json()        
        collection.insert_one(body)
        return {"data": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
