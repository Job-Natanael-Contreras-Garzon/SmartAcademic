"""
Modelos relacionados con notas y criterios de evaluación
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base

class MainApproaches(Base):
    __tablename__ = "main_approaches"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # to be, to know, to do, to decide, self-assessment
    max_weight = Column(Numeric, nullable=False)
    
    # Relación one-to-many
    subcriteria = relationship("Subcriteria", back_populates="main_approach")

class Subcriteria(Base):
    __tablename__ = "subcriteria"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Relaciones many-to-one
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    subject = relationship("Subject", back_populates="subcriteria")
    
    main_approach_id = Column(Integer, ForeignKey("main_approaches.id"))
    main_approach = relationship("MainApproaches", back_populates="subcriteria")
    
    # Relación one-to-many
    notes = relationship("SubcriteriaNote", back_populates="subcriteria")

class SubcriteriaNote(Base):
    __tablename__ = "subcriteria_notes"
    
    id = Column(Integer, primary_key=True, index=True)
    note = Column(Numeric, nullable=False)
    
    # Relaciones many-to-one
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="subcriteria_notes")
    
    subcriteria_id = Column(Integer, ForeignKey("subcriteria.id"))
    subcriteria = relationship("Subcriteria", back_populates="notes")
    
    period_id = Column(Integer, ForeignKey("periods.id"))
    period = relationship("Period", back_populates="subcriteria_notes")

class TotalNote(Base):
    __tablename__ = "total_notes"
    
    id = Column(Integer, primary_key=True, index=True)
    value_to_be = Column(Numeric, nullable=False)
    value_to_know = Column(Numeric, nullable=False)
    value_to_do = Column(Numeric, nullable=False)
    value_to_decide = Column(Numeric, nullable=False)
    value_to_self_evaluate = Column(Numeric, nullable=False)
    total = Column(Numeric, nullable=False)
    
    # Relaciones many-to-one
    student_id = Column(Integer, ForeignKey("students.id"))
    student = relationship("Student", back_populates="total_notes")
    
    period_id = Column(Integer, ForeignKey("periods.id"))
    period = relationship("Period", back_populates="total_notes")