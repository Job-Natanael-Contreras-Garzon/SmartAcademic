from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from sqlalchemy.sql import func
from app.db.base import Base
import enum

class GenderEnum(enum.Enum):
    female = "female"
    male = "male"
    other = "other"

class RoleEnum(enum.Enum):
    student = "student"
    teacher = "teacher"
    patterns = "patterns"
    administrator = "administrator"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    direction = Column(String)
    birthdate = Column(Date)
    photo = Column(String)
    last_access = Column(DateTime, default=func.now())
    gender = Column(Enum(GenderEnum))
    ci = Column(String, unique=True)
    role = Column(Enum(RoleEnum), nullable=False)
    # Relaciones con otros modelos se pueden agregar aquí según el diagrama
