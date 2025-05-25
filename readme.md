# Abre PowerShell o CMD
mkdir fastapi_demo && cd fastapi_demo

# Inicializa Git
git init

# Crea entorno virtual
python -m venv .venv

# Actívalo:
# PowerShell
.venv\Scripts\Activate.ps1

## Instalar dependencias
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary pydantic python-dotenv scikit-learn pandas
pip freeze > requirements.txt

fastapi_demo/
├── .env                            # Variables de entorno
├── .gitignore
├── requirements.txt
├── alembic.ini                     # Configuración Alembic
├── alembic/                        
│   └── versions/                   # Migraciones generadas
├── app/                            
│   ├── main.py                     # Punto de entrada de FastAPI
│   ├── core/                       
│   │   ├── config.py               # Lectura de .env y settings
│   │   ├── security.py             # Creación/verificación de JWT
│   │   └── roles.py                # Enumeración de roles y permisos
│   ├── db/                         
│   │   ├── session.py              # Configuración SQLAlchemy + PostgreSQL
│   │   └── base.py                 # Declaración de Base para modelos
│   ├── models/                     # Modelos ORM (User, Student, Teacher…)
│   ├── schemas/                    # Pydantic (validación Input/Output)
│   ├── api/                        
│   │   └── v1/                     # Versionado de la API
│   │       ├── auth.py             # /login, /refresh
│   │       ├── students.py         # CRUD de alumnos
│   │       ├── subjects.py         # CRUD de materias
│   │       ├── grades.py           # Registro de notas
│   │       ├── attendance.py       # Registro de asistencias
│   │       ├── participation.py    # Registro de participaciones
│   │       ├── prediction.py       # Endpoint de IA
│   │       └── dashboard.py        # Agregaciones para UI
│   ├── services/                   # Lógica de negocio extra
│   │   └── ml_service.py           # Carga e inferencia del modelo
│   └── dependencies.py             # FastAPI Depends (get_db, get_user…)
└── ml/                            
    ├── data/                       # Scripts para generar/simular datasets
    ├── train.py                    # Entrenamiento (RandomForest/Regresión)
    └── model.pkl                   # Modelo serializado


