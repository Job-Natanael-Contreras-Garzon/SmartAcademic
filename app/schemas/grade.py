# app/schemas/grade.py
from pydantic import BaseModel

class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    period_id: int
    total_note: float
    # teacher_id: int | None = None

class GradeCreate(GradeBase):
    pass

class GradeRead(GradeBase):
    id: int
    student_id: int
    subject_id: int
    period_id: int
    total_note: float
    # teacher_id: int | None = None

    class Config:
        orm_mode = True
