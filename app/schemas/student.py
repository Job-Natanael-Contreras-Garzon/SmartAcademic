"""
Schemas Pydantic para el modelo Student
"""
from pydantic import BaseModel
from typing import List
from .user import UserRead

class StudentBase(BaseModel):
    """Schema base para Student"""
    user_id: int
    group_id: int | None = None

class StudentCreate(StudentBase):
    """Schema para crear estudiantes"""
    pass

class StudentRead(StudentBase):
    """Schema para leer estudiantes"""
    id: int
    user: UserRead
    
    class Config:
        orm_mode = True