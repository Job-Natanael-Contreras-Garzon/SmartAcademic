from pydantic import BaseModel, validator
from typing import Optional
from decimal import Decimal

class MainApproachesBase(BaseModel):
    name: str  # to be, to know, to do, to decide, self-assessment
    max_weight: Decimal
    
    @validator('max_weight')
    def validate_weight(cls, v):
        if v < 0 or v > 100:
            raise ValueError('Weight must be between 0 and 100')
        return v

class MainApproachesCreate(MainApproachesBase):
    pass

class MainApproachesUpdate(BaseModel):
    name: Optional[str] = None
    max_weight: Optional[Decimal] = None

class MainApproachesRead(MainApproachesBase):
    id: int
    
    class Config:
        from_attributes = True
