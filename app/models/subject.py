"""
Modelo Subject y tablas de asociación
Representa las materias y sus relaciones
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.db.base import Base

# Tabla de asociación many-to-many entre Student y Subject
student_subject = Table(
    'student_subject',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('subject_id', Integer, ForeignKey('subjects.id'), primary_key=True)
)

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Relaciones many-to-many
    students = relationship("Student", secondary=student_subject, back_populates="subjects")
    
    # Relación one-to-many
    subcriteria = relationship("Subcriteria", back_populates="subject")

    def __repr__(self):
        return f"<Subject {self.name}>"