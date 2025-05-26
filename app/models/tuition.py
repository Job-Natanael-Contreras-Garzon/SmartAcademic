"""
Modelos para gestión de matrículas y pagos
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship
from app.db.base import Base
from .enums import TuitionStatusEnum

class Tuition(Base):
    __tablename__ = "tuitions"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL, nullable=False)
    month = Column(String, nullable=False)
    status = Column(Enum(TuitionStatusEnum), nullable=False)
    
    # Relación one-to-many
    student_tuitions = relationship("StudentTuition", back_populates="tuition")
    
    def __repr__(self):
        return f"<Tuition {self.month} - {self.status.value}>"

class StudentTuition(Base):
    __tablename__ = "student_tuitions"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Relaciones many-to-one
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="tuitions")
    
    tuition_id = Column(Integer, ForeignKey("tuitions.id"))
    tuition = relationship("Tuition", back_populates="student_tuitions")
    
    def __repr__(self):
        return f"<StudentTuition {self.student_id} - {self.tuition_id}>"