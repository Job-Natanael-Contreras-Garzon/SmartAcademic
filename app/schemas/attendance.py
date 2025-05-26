# app/schemas/attendance.py
from pydantic import BaseModel
from datetime import date

class AttendanceBase(BaseModel):
    student_id: int
    date: date
    present: bool = False

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceRead(AttendanceBase):
    id: int
    student_id: int
    date: date
    present: bool

    class Config:
        orm_mode = True
