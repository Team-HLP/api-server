from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorDatabase
from datebase import get_mongodb, get_mysql
from gaze.models import GazeData, GazePacket
from typing import List
from user.models import User
from user.auth import get_current_user

router = APIRouter()

@router.post("", status_code=201)
async def save_gaze_date(
    packet: GazePacket,
    db: AsyncIOMotorDatabase = Depends(get_mongodb)
    # current_user: User = Depends(get_current_user),
):
    docs = [d.model_dump() for d in packet.data]
    for doc in docs:
        doc["user_id"] = packet.user_id
        doc["game_id"] = packet.game_id

    result = await db["gazes"].insert_many(docs)
    return {"inserted": len(result.inserted_ids)}

@router.get("", response_model=GazePacket)
async def get_gaze_data(
    user_id: int = Query(...),
    game_id: int = Query(...),
    db: AsyncIOMotorDatabase = Depends(get_mongodb)
):
    cursor = db["gazes"].find({
        "user_id": user_id,
        "game_id": game_id
    })

    gaze_data = []
    async for doc in cursor:
        gaze_data.append(GazeData(
            timestamp=doc["timestamp"],
            x=doc["x"],
            y=doc["y"],
            z=doc["z"]
        ))

    if not gaze_data:
        raise HTTPException(status_code=404, detail="No gaze data found for given user/game.")

    return GazePacket(
        user_id=user_id,
        game_id=game_id,
        data=gaze_data
    )
