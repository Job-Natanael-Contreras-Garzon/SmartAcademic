# app/schemas/subject.py
from pydantic import BaseModel

class SubjectBase(BaseModel):
    name: str
    # teacher_id: int | None = None # Optional if a subject can exist without an assigned teacher

class SubjectCreate(SubjectBase):
    pass

class SubjectRead(SubjectBase):
    id: int
    # teacher_id: int | None = None

    class Config:
        orm_mode = True
