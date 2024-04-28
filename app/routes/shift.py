from fastapi import APIRouter, HTTPException
from app.models.shift import Shift, ShiftCreate
from app.database.connection import startup_db_client, close_db_client

router = APIRouter()

@router.post("/shifts/", response_model=Shift)
async def create_shift(shift: ShiftCreate):
    db = await startup_db_client()
    try:
        collection = db["shifts"]
        result = await collection.insert_one(shift.dict())
        created_shift = await collection.find_one({"_id": result.inserted_id})
        if created_shift:
            return created_shift
        else:
            raise HTTPException(status_code=500, detail="Failed to create shift")
    finally:
        await close_db_client()

@router.get("/shifts/", response_model=list[Shift])
async def get_shifts():
    db = await startup_db_client()
    try:
        collection = db["shifts"]
        shifts = await collection.find().to_list(length=100)
        return shifts
    finally:
        await close_db_client()
