# app/schemas/user.py (Actualizado)
from pydantic import BaseModel, EmailStr
from datetime import date
from app.core.roles import Role # Asegúrate de que Role está definido aquí o importado correctamente

class UserBase(BaseModel):
    code: str | None = None # Puede ser nulo al crear si se genera automáticamente
    name: str
    last_name: str
    phone: str | None = None
    email: EmailStr
    direction: str | None = None
    birthdate: date | None = None
    photo: str | None = None
    gender: str | None = None # Considerar usar un Enum aquí también
    ci: str | None = None # Cédula de identidad
    role: Role # Usando el Enum de roles

class UserCreate(UserBase):
    # Puedes añadir campos específicos para la creación, como password
    password: str

class UserRead(UserBase):
    id: int
    last_access: date | None = None # Incluir campos que no están en Create pero sí en la BD

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    # Esquema para actualizar (todos los campos son opcionales)
    code: str | None = None
    name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    email: EmailStr | None = None
    direction: str | None = None
    birthdate: date | None = None
    photo: str | None = None
    gender: str | None = None
    ci: str | None = None
    role: Role | None = None
