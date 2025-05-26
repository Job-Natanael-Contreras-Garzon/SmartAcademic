"""
Modelo para gestionar la relación entre estudiantes y tutores
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class StudentTutor(Base):
    __tablename__ = "student_tutors"
    
    id = Column(Integer, primary_key=True, index=True)
    relation_type = Column(String, nullable=False)  # tutor, partner, etc.
    
    # Relaciones many-to-one
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="tutors")
    
    def __repr__(self):
        return f"<StudentTutor {self.relationship}>"