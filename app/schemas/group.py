"""
Schemas Pydantic para el modelo Group
"""
from pydantic import BaseModel
from app.models.enums import GradeEnum, LevelEnum

class GroupBase(BaseModel):
    """Schema base para Group"""
    grade: GradeEnum
    level: LevelEnum
    group: str  # A, B, C, D, E, F

class GroupCreate(GroupBase):
    """Schema para crear grupos"""
    pass

class GroupRead(GroupBase):
    """Schema para leer grupos"""
    id: int
    
    class Config:
        orm_mode = True