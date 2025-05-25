from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Crear el engine de conexión a PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
)

# Crear una clase SessionLocal para instanciar sesiones
db_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependencia para inyectar la sesión en los endpoints
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()