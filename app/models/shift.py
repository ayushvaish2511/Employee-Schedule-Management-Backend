# app/models/shift.py

from pydantic import BaseModel
from typing import List

class ShiftBase(BaseModel):
    start_time: str
    end_time: str
    department: str
    required_skills: List[str]

class ShiftCreate(ShiftBase):
    pass

class Shift(ShiftBase):
    id: str

    class Config:
        orm_mode = True
