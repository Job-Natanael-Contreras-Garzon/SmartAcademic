from typing import Optional
from pydantic import BaseModel
from enum import Enum

class GradeEnum(str, Enum):
    first = "1ro"
    second = "2do"
    third = "3ro"
    fourth = "4to"
    fifth = "5to"
    sixth = "6to"
    kinder = "kinder"
    prekinder = "prekinder"

class LevelEnum(str, Enum):
    initial = "initial"
    primary = "primary"
    secondary = "secondary"

class GroupBase(BaseModel):
    grade: GradeEnum
    level: LevelEnum
    group: str

class GroupCreate(GroupBase):
    pass

class GroupRead(GroupBase):
    id: int

    class Config:
        from_attributes = True
