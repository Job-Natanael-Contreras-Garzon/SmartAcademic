"""
Modelo User siguiendo el diagrama de clases UML
Representa la entidad principal del sistema
"""
from sqlalchemy import Column, Integer, String, Date, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base
from .enums import GenderEnum, RoleEnum

class User(Base):
    __tablename__ = "users"
    
    # Campos básicos
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    direction = Column(String)
    birthdate = Column(Date)
    photo = Column(String)
    last_access = Column(DateTime, default=datetime.utcnow)
    
    # Enumeraciones
    gender = Column(Enum(GenderEnum), nullable=False)
    ci = Column(String, unique=True, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    # Relaciones one-to-one según el diagrama
    student = relationship("Student", back_populates="user", uselist=False)
    teacher = relationship("Teacher", back_populates="user", uselist=False)

    # Relaciones many-to-many
    groups = relationship("Group", 
                        secondary="user_group",
                        back_populates="users")

    def __repr__(self):
        return f"<User {self.name} {self.last_name}>"