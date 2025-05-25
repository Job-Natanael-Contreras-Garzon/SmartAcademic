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