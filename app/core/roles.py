from enum import Enum

class Role(str, Enum):
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"

ROLE_PERMISSIONS = {
    Role.ADMIN:   ["students:crud", "subjects:crud", "grades:crud", "attendance:crud", "participation:crud"],
    Role.TEACHER: ["grades:write", "attendance:write", "participation:write"],
    Role.STUDENT: ["grades:read", "attendance:read", "participation:read"],
}