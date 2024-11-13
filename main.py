from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import os

app = FastAPI()

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["analytics"]
collection = db["analytics"]
locationsCollection = db["locations"]

@app.get("/ping")
async def ping():
    return JSONResponse(content={"message": "Pong"})

@app.post("/")
async def analytics(request: Request):
    try:
        body = await request.json()        
        collection.insert_one(body)
        return JSONResponse(content={"data": True})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/location")
async def add_location(
    latitude: float = Query(None,),
    longitude: float = Query(None),
    time: int = Query(None)
    ):
    try: 
        location_data = {
            "latitude": latitude,
            "longitude": longitude,
            "time": time
        }
        locationsCollection.insert_one(location_data)
        return JSONResponse(content={"data": True})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))