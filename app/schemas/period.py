# app/schemas/period.py
from pydantic import BaseModel

class PeriodBase(BaseModel):
    name: str

class PeriodCreate(PeriodBase):
    pass

class PeriodRead(PeriodBase):
    id: int

    class Config:
        orm_mode = True
