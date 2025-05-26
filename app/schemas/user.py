"""
Schemas Pydantic para el modelo User
"""
from datetime import date
from pydantic import BaseModel, EmailStr
from app.models.enums import GenderEnum, RoleEnum

class UserBase(BaseModel):
    """Schema base para User"""
    code: str
    name: str
    last_name: str
    phone: str | None = None
    email: EmailStr
    direction: str | None = None
    birthdate: date | None = None
    photo: str | None = None
    gender: GenderEnum
    ci: str
    role: RoleEnum

class UserCreate(UserBase):
    """Schema para crear usuarios"""
    password: str

class UserRead(UserBase):
    """Schema para leer usuarios"""
    id: int
    
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    """Schema para actualizar usuarios"""
    code: str | None = None
    name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    direction: str | None = None
    birthdate: date | None = None
    photo: str | None = None
    gender: GenderEnum | None = None
    ci: str | None = None
    role: RoleEnum | None = None