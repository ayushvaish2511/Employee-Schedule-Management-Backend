from fastapi import APIRouter, HTTPException
from typing import List
from app.models.schedule import ShiftAssignment, Schedule
from app.database.connection import startup_db_client, close_db_client

router = APIRouter()

@router.post("/employees/{employee_id}/assign-shift/", response_model=ShiftAssignment)
async def assign_shift_to_employee(employee_id: str, shift_id: str):
    db = await startup_db_client()
    try:
        collection = db["shift_assignments"]
        result = await collection.insert_one({"employee_id": employee_id, "shift_id": shift_id})
        if result.inserted_id:
            assignment = ShiftAssignment(employee_id=employee_id, shift_id=shift_id)
            return assignment
        else:
            raise HTTPException(status_code=500, detail="Failed to assign shift to employee")
    finally:
        await close_db_client()

@router.get("/employees/{employee_id}/schedule/", response_model=Schedule)
async def get_employee_schedule(employee_id: str):
    db = await startup_db_client()
    try:
        collection = db["shift_assignments"]
        employee_schedule = []
        async for shift_assignment in collection.find({"employee_id": employee_id}):
            employee_schedule.append(ShiftAssignment(**shift_assignment))
        schedule = Schedule(employee_id=employee_id, shifts=employee_schedule)
        return schedule
    finally:
        await close_db_client()
