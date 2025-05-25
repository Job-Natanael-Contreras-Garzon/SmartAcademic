# FastAPI + PostgreSQL + JWT Demo

> **Nota del autor:**
> Como es mi primera vez trabajando con FastAPI, he incluido comentarios y explicaciones adicionales para entender mejor cada paso.

Proyecto demo paso a paso para construir un back-end en FastAPI con:

* Base de datos PostgreSQL
* Autenticación y autorización con JWT
* Roles de acceso (ADMIN, TEACHER, STUDENT)
* Módulo de Machine Learning para predicción de rendimiento

---

## Tabla de Contenidos

1. [Inicialización del proyecto](#sección-1-inicialización-del-proyecto)
2. [Configuración y utilidades centrales](#sección-2-configuración-y-utilidades-centrales)
3. [Conexión a la base de datos](#sección-3-conexión-a-la-base-de-datos)
4. [Modelos ORM y esquemas Pydantic](#sección-4-modelos-orm-y-esquemas-pydantic)
5. [Migraciones automáticas](#sección-5-migraciones-automáticas)
6. [Autenticación y control de acceso](#sección-6-autenticación-y-control-de-acceso)
7. [Endpoints CRUD básicos](#sección-7-endpoints-crud-básicos)
8. [Módulo de Machine Learning](#sección-8-módulo-de-machine-learning)
9. [Endpoint de predicción](#sección-9-endpoint-de-predicción)
10. [Dashboard y agregaciones](#sección-10-dashboard-y-agregaciones)
11. [Pruebas y documentación](#sección-11-pruebas-y-documentación)
12. [Despliegue y contenedorización](#sección-12-despliegue-y-contenedorización)
13. [Estructura de Carpetas](#estructura-de-carpetas)
14. [Catálogo de Endpoints](#catálogo-de-endpoints)

---

## Sección 1: Inicialización del proyecto

**Objetivo:** Preparar el entorno y estructura básica.

> **Comentario (principiante):**
> Configuro todo desde cero porque es mi primera vez usando FastAPI.

**Pasos completados:**

1. Instalación de prerrequisitos: Python 3.10+, Git, PostgreSQL, VS Code.
2. Creación de carpeta `fastapi_demo/` y control de versiones (`git init`).
3. Entorno virtual (`python -m venv .venv`; activación).
4. Instalación de dependencias:

   ```bash
   pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary pydantic python-dotenv scikit-learn pandas
   pip freeze > requirements.txt
   ```
5. Archivo `.env` con variables críticas.
6. Estructura de carpetas inicial.
7. Configuración de Alembic y migración inicial.
8. Esqueleto de `app/main.py` con routers básicos.

---

## Sección 2: Configuración y utilidades centrales

**Archivos en `app/core/`:**

* **config.py**: lectura de `.env` con Pydantic.
* **security.py**: funciones `create_access_token` y `verify_token` (JWT HS256).
* **roles.py**: definición de `Role` y `ROLE_PERMISSIONS`.

---

## Sección 3: Conexión a la base de datos

**Archivos en `app/db/`:**

* **session.py**: configuración de `engine`, `SessionLocal` y dependencia `get_db()`.
* **base.py**: declaración de `Base` para modelos SQLAlchemy.

---

## Sección 4: Modelos ORM y esquemas Pydantic

**Modelos** (`app/models/`) según el diagrama de clases:

* `User`, `Student`, `Teacher`, `Admin`, `Subject`, `Grade`, `Attendance`, `Participation`.

**Esquemas** (`app/schemas/`):

* Para cada modelo: `Base`, `Create`, `Read` con `orm_mode=True`.

---

## Sección 5: Migraciones automáticas

1. Configurar `alembic.ini` y `env.py` para usar `Base.metadata`.
2. Generar migraciones: `alembic revision --autogenerate -m "Mensaje"`.
3. Aplicar migraciones: `alembic upgrade head`.

---

## Sección 6: Autenticación y control de acceso

* Ruta `/api/v1/auth/login`: validación de credenciales y emisión de JWT.
* Dependencias en `app/dependencies.py` para extraer `current_user` y verificar roles.

---

## Sección 7: Endpoints CRUD básicos

Routers en `app/api/v1/` para CRUD de:

* `students`
* `subjects`
* `grades`
* `attendance`
* `participation`

---

## Sección 8: Módulo de Machine Learning

* `ml/train.py`: entrenamiento con `RandomForestRegressor` y serialización con `joblib`.
* `app/services/ml_service.py`: carga de `model.pkl` y función `predict_student`.

---

## Sección 9: Endpoint de predicción

* Ruta `/api/v1/prediction`: recibe datos de un alumno y devuelve predicción numérica y categórica.

---

## Sección 10: Dashboard y agregaciones

* Ruta `/api/v1/dashboard`: estadísticas agregadas (total alumnos, promedio, comparativa real vs predicho).

---

## Sección 11: Pruebas y documentación

* Usar `pytest` o `HTTPX` para tests.
* Swagger UI disponible en `/docs` y ReDoc en `/redoc`.

---

## Sección 12: Despliegue y contenedorización

* **Dockerfile** para FastAPI + uvicorn.
* **docker-compose.yml** con servicios `web` y `db` (PostgreSQL).

---

## Estructura de Carpetas

```plaintext
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
```

---

## Catálogo de Endpoints

A continuación se describen los endpoints principales, su funcionalidad y ejemplos de uso.

### 1. Gestión de Alumnos

* **Listar alumnos**

  * **Método:** GET
  * **Ruta:** `/api/v1/students/`
  * **Descripción:** Devuelve todos los registros de alumnos.
  * **Respuesta (200):**

    ```json
    [
      {"id":1,"user_id":1},
      {"id":2,"user_id":2}
    ]
    ```

* **Crear alumno**

  * **Método:** POST
  * **Ruta:** `/api/v1/students/`
  * **Cuerpo:**

    ```json
    {"user_id":3}
    ```
  * **Respuesta (201):**

    ```json
    {"id":3,"user_id":3}
    ```

* **Obtener alumno**

  * **Método:** GET
  * **Ruta:** `/api/v1/students/{id}`
  * **Respuesta (200):**

    ```json
    {"id":1,"user_id":1}
    ```

* **Actualizar alumno**

  * **Método:** PUT
  * **Ruta:** `/api/v1/students/{id}`
  * **Cuerpo:**

    ```json
    {"user_id":4}
    ```
  * **Respuesta (200):**

    ```json
    {"id":1,"user_id":4}
    ```

* **Eliminar alumno**

  * **Método:** DELETE
  * **Ruta:** `/api/v1/students/{id}`
  * **Respuesta (204):** No content

### 2. Gestión de Materias

Endpoints análogos a alumnos, reemplazando `students` por `subjects` y campos específicos (p.ej. nombre, código).

### 3. Registro de Notas

* **Registrar nota**

  * **Método:** POST
  * **Ruta:** `/api/v1/grades/`
  * **Cuerpo:**

    ```json
    {
      "student_id":1,
      "subject_id":2,
      "period_id":1,
      "total_note":85.5
    }
    ```
  * **Respuesta (201):**

    ```json
    {"id":5,"total_note":85.5}
    ```

### 4. Registro de Asistencia

* **Registrar asistencia**

  * **Método:** POST
  * **Ruta:** `/api/v1/attendance/`
  * **Cuerpo:**

    ```json
    {"student_id":1,"date":"2025-05-25","present":true}
    ```
  * **Respuesta (201):**

    ```json
    {"id":10,"present":true}
    ```

### 5. Registro de Participaciones

* **Registrar participación**

  * **Método:** POST
  * **Ruta:** `/api/v1/participation/`
  * **Cuerpo:**

    ```json
    {"student_id":1,"session_id":3,"score":4}
    ```
  * **Respuesta (201):**

    ```json
    {"id":7,"score":4}
    ```

### 6. Predicción del rendimiento (IA)

* **Obtener predicción**

  * **Método:** POST
  * **Ruta:** `/api/v1/prediction/`
  * **Cuerpo:**

    ```json
    {"nota_promedio":75.0,"asistencia_pct":92.5,"participacion_prom":3.5}
    ```
  * **Respuesta (200):**

    ```json
    {"prediccion":81.2,"categoria":"alto"}
    ```

### 7. Dashboard y agregaciones

* **Obtener estadísticas**

  * **Método:** GET
  * **Ruta:** `/api/v1/dashboard/`
  * **Respuesta (200):**

    ```json
    {
      "total_students":120,
      "average_grade":78.3,
      "real_vs_predicted": [
        {"actual":75,"predicted":80},
        {"actual":82,"predicted":85}
      ]
    }
    ```

---

## Documentación Swagger

FastAPI expone automáticamente **Swagger UI** en:

```
http://localhost:8000/docs
```

Y **ReDoc** en:

```
http://localhost:8000/redoc
```

---

*Fin del README.md*
