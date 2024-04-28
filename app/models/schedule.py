from pydantic import BaseModel
from typing import List

class ShiftAssignment(BaseModel):
    employee_id: str
    shift_id: str

class Schedule(BaseModel):
    employee_id: str
    shifts: List[ShiftAssignment]
