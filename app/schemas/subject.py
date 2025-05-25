from pydantic import BaseModel
from typing import Optional, List

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(SubjectBase):
    pass

class SubjectRead(SubjectBase):
    id: int
    
    class Config:
        from_attributes = True
