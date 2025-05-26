"""
Schemas Pydantic para los modelos relacionados con notas
"""
from pydantic import BaseModel, condecimal, Field
from typing import List, Optional, Annotated
from decimal import Decimal

class MainApproachesBase(BaseModel):
    """Schema base para MainApproaches"""
    name: str = Field(..., description="Nombre del enfoque principal")
    max_weight: Annotated[Decimal, Field(..., description="Peso máximo del criterio")]  # condecimal constraint will be handled in validation or by using a custom validator

    class Config:
        json_schema_extra = {
            "example": {
                "name": "to_be",
                "max_weight": 20.00
            }
        }

class SubcriteriaBase(BaseModel):
    """Schema base para Subcriteria"""
    name: str
    subject_id: int
    main_approach_id: int

class SubcriteriaNoteBase(BaseModel):
    """Schema base para SubcriteriaNote"""
    note: Annotated[Decimal, Field(..., ge=0, le=100)]
    student_id: int
    subcriteria_id: int
    period_id: int

class TotalNoteBase(BaseModel):
    """Schema base para TotalNote"""
    value_to_be: Annotated[Decimal, Field(..., ge=0, le=100)]
    value_to_know: Annotated[Decimal, Field(..., ge=0, le=100)]
    value_to_do: Annotated[Decimal, Field(..., ge=0, le=100)]
    value_to_decide: Annotated[Decimal, Field(..., ge=0, le=100)]
    value_to_self_evaluate: Annotated[Decimal, Field(..., ge=0, le=100)]
    total: Annotated[Decimal, Field(..., ge=0, le=100)]
    student_id: int
    period_id: int

    class Config:
        orm_mode = True