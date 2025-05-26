"""
Exportación de todos los schemas Pydantic
"""
from .user import UserBase, UserCreate, UserRead, UserUpdate
from .student import StudentBase, StudentCreate, StudentRead
from .group import GroupBase, GroupCreate, GroupRead
from .note import (
    MainApproachesBase,
    SubcriteriaBase,
    SubcriteriaNoteBase,
    TotalNoteBase
)
from .period import PeriodBase, PeriodCreate, PeriodRead
from .tuition import (
    TuitionBase,
    TuitionCreate,
    TuitionRead,
    StudentTuitionBase,
    StudentTuitionCreate,
    StudentTuitionRead
)

__all__ = [
    "UserBase",
    "UserCreate",
    "UserRead",
    "UserUpdate",
    "StudentBase",
    "StudentCreate",
    "StudentRead",
    "GroupBase",
    "GroupCreate",
    "GroupRead",
    "MainApproachesBase",
    "SubcriteriaBase",
    "SubcriteriaNoteBase",
    "TotalNoteBase",
    "PeriodBase",
    "PeriodCreate",
    "PeriodRead",
    "TuitionBase",
    "TuitionCreate",
    "TuitionRead",
    "StudentTuitionBase",
    "StudentTuitionCreate",
    "StudentTuitionRead"
]