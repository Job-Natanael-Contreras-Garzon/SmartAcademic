"""
Modelo Group y tabla de asociación UserGroup
Representa los grupos escolares y su relación con usuarios
"""
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base
from .enums import GradeEnum, LevelEnum

# Tabla de asociación many-to-many entre User y Group
user_group = Table(
    'user_group',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('group_id', Integer, ForeignKey('groups.id'), primary_key=True)
)

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    grade = Column(Enum(GradeEnum), nullable=False)
    level = Column(Enum(LevelEnum), nullable=False)
    group = Column(String, nullable=False)  # A, B, C, D, E, F

    # Relaciones
    users = relationship("User", 
                      secondary=user_group,
                      back_populates="groups")
    students = relationship("Student", back_populates="group")

    def __repr__(self):
        return f"<Group {self.grade.value} {self.group}>"