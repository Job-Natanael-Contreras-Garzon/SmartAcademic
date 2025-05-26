"""
Modelo Period para gestionar períodos académicos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Period(Base):
    __tablename__ = "periods"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Relaciones one-to-many
    total_notes = relationship("TotalNote", back_populates="period")
    subcriteria_notes = relationship("SubcriteriaNote", back_populates="period")
    
    def __repr__(self):
        return f"<Period {self.name}>"