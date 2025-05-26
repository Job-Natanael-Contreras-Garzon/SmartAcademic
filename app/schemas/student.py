# app/schemas/student.py (Actualizado)
from pydantic import BaseModel

class StudentBase(BaseModel):
    user_id: int

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int
    user_id: int # Incluir user_id para la respuesta

    class Config:
        orm_mode = True
