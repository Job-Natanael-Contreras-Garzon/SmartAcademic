"""
Enumeraciones utilizadas en los modelos
Siguiendo el diagrama de clases UML
"""
from enum import Enum

class GenderEnum(str, Enum):
    """Género del usuario"""
    female = "female"
    male = "male"
    other = "other"

class RoleEnum(str, Enum):
    """Roles de usuario según el diagrama"""
    student = "student"
    teacher = "teacher"
    patterns = "patterns"
    administrator = "administrator"

class GradeEnum(str, Enum):
    """Grados escolares"""
    first = "1ro"
    second = "2do"
    third = "3ro"
    fourth = "4to"
    fifth = "5to"
    sixth = "6to"
    kinder = "kinder"
    prekinder = "prekinder"

class LevelEnum(str, Enum):
    """Niveles educativos"""
    initial = "initial"
    primary = "primary"
    secondary = "secondary"

class TuitionStatusEnum(str, Enum):
    """Estados de pago"""
    paid = "paid"
    pending = "pending"
    overdue = "overdue"