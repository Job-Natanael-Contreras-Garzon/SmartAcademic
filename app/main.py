from fastapi import FastAPI
from app.api.v1 import auth, students, subjects  # etc.

app = FastAPI(title="Demo FastAPI + JWT + PostgreSQL")

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(students.router, prefix="/api/v1/students")
# ... demás routers ...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)