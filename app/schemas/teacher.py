# app/schemas/teacher.py
from pydantic import BaseModel

class TeacherBase(BaseModel):
    user_id: int

class TeacherCreate(TeacherBase):
    pass

class TeacherRead(TeacherBase):
    id: int

    class Config:
        orm_mode = True # Habilitar compatibilidad con ORM
