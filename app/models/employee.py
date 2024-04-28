# app/models/employee.py

from pydantic import BaseModel
from typing import List

class EmployeeBase(BaseModel):
    name: str
    department: str
    role: str
    availability: List[str]

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: str

    class Config:
        orm_mode = True
