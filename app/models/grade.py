# app/models/grade.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    period_id = Column(Integer, ForeignKey("periods.id"))
    total_note = Column(Float) # Assuming this is the final calculated grade for the period/subject
    # teacher_id = Column(Integer, ForeignKey("teachers.id")) # Optional: if we want to track which teacher registered the grade

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
    period = relationship("Period", back_populates="grades")
    # teacher = relationship("Teacher", back_populates="grades")
    # subcriteria_notes = relationship("Subcriteria_Note", back_populates="grade")
