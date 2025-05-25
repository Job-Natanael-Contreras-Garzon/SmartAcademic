from typing import Optional
from pydantic import BaseModel
from .user import UserRead
from .group import GroupRead

class StudentBase(BaseModel):
    user_id: int
    group_id: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int
    user: UserRead
    group: Optional[GroupRead] = None

    class Config:
        from_attributes = True
