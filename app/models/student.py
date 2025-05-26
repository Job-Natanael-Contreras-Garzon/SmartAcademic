"""
Modelo Student y sus relaciones
Siguiendo el diagrama de clases UML
"""
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)

    # Relación one-to-one con User
    user = relationship("User", back_populates="student")
    
    # Relación many-to-one con Group
    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group", back_populates="students")
    
    # Relaciones one-to-many
    total_notes = relationship("TotalNote", back_populates="student")
    subcriteria_notes = relationship("SubcriteriaNote", back_populates="student")
    
    # Relaciones many-to-many
    subjects = relationship("Subject", secondary="student_subject", back_populates="students")
    tutors = relationship("StudentTutor", back_populates="student")
    tuitions = relationship("StudentTuition", back_populates="student")

    def __repr__(self):
        return f"<Student {self.user.name} {self.user.last_name}>"