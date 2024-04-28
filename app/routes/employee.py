from fastapi import APIRouter, HTTPException
from app.models.employee import Employee, EmployeeCreate
from app.database.connection import startup_db_client, close_db_client

router = APIRouter()

@router.post("/employees/", response_model=Employee)
async def create_employee(employee: EmployeeCreate):
    db = await startup_db_client()
    try:
        collection = db["employees"]
        result = await collection.insert_one(employee.dict())
        created_employee = await collection.find_one({"_id": result.inserted_id})
        if created_employee:
            return created_employee
        else:
            raise HTTPException(status_code=500, detail="Failed to create employee")
    finally:
        await close_db_client()

@router.put("/employees/{employee_id}/", response_model=Employee)
async def update_employee(employee_id: str, employee_update: EmployeeCreate):
    db = await startup_db_client()
    try:
        collection = db["employees"]
        employee = await collection.find_one({"_id": employee_id})
        if employee:
            await collection.update_one({"_id": employee_id}, {"$set": employee_update.dict()})
            updated_employee = await collection.find_one({"_id": employee_id})
            return updated_employee
        else:
            raise HTTPException(status_code=404, detail="Employee not found")
    finally:
        await close_db_client()
