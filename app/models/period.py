# app/models/period.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Period(Base):
    __tablename__ = "periods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # e.g., "Primer Trimestre", "Segundo Semestre"

    grades = relationship("Grade", back_populates="period")
    # total_notes = relationship("Total_Note", back_populates="period")
