# app/models/student.py (Actualizado)
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    user = relationship("User", back_populates="student")
    grades = relationship("Grade", back_populates="student")
    attendance_records = relationship("Attendance", back_populates="student")
    participation_records = relationship("Participation", back_populates="student")
    # student_tutors = relationship("Student_Tutor", back_populates="student")
    # student_tuitions = relationship("Student_Tuition", back_populates="student")