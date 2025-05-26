# app/models/subject.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # teacher_id = Column(Integer, ForeignKey("teachers.id")) # Assuming a subject is taught by one teacher

    # teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")
    # subcriteria = relationship("Subcriteria", back_populates="subject")
