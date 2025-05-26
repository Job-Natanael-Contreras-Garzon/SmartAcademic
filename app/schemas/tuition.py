"""
Schemas Pydantic para los modelos Tuition y StudentTuition
"""
from pydantic import BaseModel, condecimal
from app.models.enums import TuitionStatusEnum
from typing import Optional, Annotated

class TuitionBase(BaseModel):
    """Schema base para Tuition"""
    amount: Annotated[float, condecimal(gt=0)]
    month: str
    status: TuitionStatusEnum

class TuitionCreate(TuitionBase):
    """Schema para crear matrículas"""
    pass

class TuitionRead(TuitionBase):
    """Schema para leer matrículas"""
    id: int

    class Config:
        orm_mode = True

class StudentTuitionBase(BaseModel):
    """Schema base para StudentTuition"""
    student_id: int
    tuition_id: int

class StudentTuitionCreate(StudentTuitionBase):
    """Schema para crear relación estudiante-matrícula"""
    pass

class StudentTuitionRead(StudentTuitionBase):
    """Schema para leer relación estudiante-matrícula"""
    id: int
    tuition: TuitionRead

    class Config:
        orm_mode = True