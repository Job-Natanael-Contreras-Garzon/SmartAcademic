# app/schemas/participation.py
from pydantic import BaseModel

class ParticipationBase(BaseModel):
    student_id: int
    # session_id: int # Assuming some identifier for the session/class
    score: float

class ParticipationCreate(ParticipationBase):
    pass

class ParticipationRead(ParticipationBase):
    id: int
    student_id: int
    # session_id: int
    score: float

    class Config:
        orm_mode = True
