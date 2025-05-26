# app/schemas/admin.py
from pydantic import BaseModel

class AdminBase(BaseModel):
    user_id: int

class AdminCreate(AdminBase):
    pass

class AdminRead(AdminBase):
    id: int

    class Config:
        orm_mode = True
