# app/models/participation.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Participation(Base):
    __tablename__ = "participation"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    # session_id = Column(Integer) # Assuming some kind of session or class identifier
    score = Column(Float) # Score or measure of participation

    student = relationship("Student", back_populates="participation_records")
