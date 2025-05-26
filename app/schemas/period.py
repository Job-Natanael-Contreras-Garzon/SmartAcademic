"""
Schemas Pydantic para el modelo Period
"""
from pydantic import BaseModel
from typing import List, Optional
from .note import TotalNoteBase, SubcriteriaNoteBase

class PeriodBase(BaseModel):
    """Schema base para Period"""
    name: str

class PeriodCreate(PeriodBase):
    """Schema para crear períodos"""
    pass

class PeriodRead(PeriodBase):
    """Schema para leer períodos"""
    id: int
    total_notes: Optional[List[TotalNoteBase]] = []
    subcriteria_notes: Optional[List[SubcriteriaNoteBase]] = []

    class Config:
        orm_mode = True