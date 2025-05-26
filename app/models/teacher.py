# app/models/teacher.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="teacher")
    subjects = relationship("Subject", back_populates="teacher")
    grades = relationship("Grade", back_populates="teacher") # Assuming teachers register grades
