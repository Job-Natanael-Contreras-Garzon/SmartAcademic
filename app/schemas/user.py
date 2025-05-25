from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, validator
from enum import Enum

class GenderEnum(str, Enum):
    female = "female"
    male = "male"
    other = "other"

class RoleEnum(str, Enum):
    student = "student"
    teacher = "teacher"
    patterns = "patterns"
    administrator = "administrator"

class UserBase(BaseModel):
    code: str
    name: str
    last_name: str
    phone: Optional[str] = None
    email: EmailStr
    direction: Optional[str] = None
    birthdate: Optional[date] = None
    gender: Optional[GenderEnum] = None
    ci: Optional[str] = None
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserRead(UserBase):
    id: int
    photo: Optional[str] = None
    last_access: Optional[datetime] = None
    
    class Config:
        from_attributes = True  # Para compatibilidad con SQLAlchemy
