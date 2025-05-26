# alembic/env.py

from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
# Eliminamos la importación de declarative_base, ya que importamos Base desde nuestro archivo base.py
# from sqlalchemy.orm import declarative_base # ELIMINAR O COMENTAR ESTA LINEA

from alembic import context

# --- COMIENZO DE LA SECCIÓN DE RUTA ---
# Importaciones estándar de Python necesarias para la ruta
import os
import sys

# Añade el directorio raíz del proyecto al sys.path.
# Esto DEBE ejecutarse ANTES de importar cualquier módulo desde 'app.*'
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# --- FIN DE LA SECCIÓN DE RUTA ---


# Importa tu Base declarativa de SQLAlchemy desde nuestro archivo base.py.
# Esta importación ahora se ejecutará DESPUÉS de que el directorio del proyecto se haya añadido a sys.path.
from app.db.base import Base # Asegúrate de que esta importación sea correcta

# Importa TODOS tus modelos aquí. Esto es CRUCIAL para que Base.metadata
# contenga la información de todas tus tablas y Alembic pueda detectarlas
# para las migraciones automáticas ('autogenerate').
# Estas importaciones ahora se ejecutarán DESPUÉS de que el directorio del proyecto se haya añadido a sys.path.
from app.models.user import User  # noqa
from app.models.student import Student # noqa
from app.models.teacher import Teacher # noqa
from app.models.admin import Admin # noqa
from app.models.subject import Subject # noqa
from app.models.period import Period # noqa
from app.models.grade import Grade # noqa
from app.models.attendance import Attendance # noqa
from app.models.participation import Participation # noqa
# Asegúrate de importar aquí cualquier otro modelo que hayas creado en app/models/
# Por ejemplo:
# from app.models.group import Group # noqa
# from app.models.main_approaches import Main_approaches # noqa
# from app.models.subcriteria import Subcriteria # noqa
# from app.models.subcriteria_note import Subcriteria_Note # noqa
# from app.models.total_note import Total_Note # noqa
# from app.models.student_tutor import Student_Tutor # noqa
# from app.models.tuition import Tuition # noqa
# from app.models.student_tuition import Student_Tuition # noqa
# from app.models.user_group import User_Group # noqa


# Mantenemos las líneas para imprimir sys.path para depuración.
# Si la importación de Base tiene éxito, veremos esto impreso.
import pprint # Importa pprint para imprimir la lista sys.path de forma más legible

print("Contenido de sys.path ANTES de configurar Alembic:")
pprint.pprint(sys.path)


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is still acceptable
    here as values can be acquired from the config file.

    By skipping the Engine creation we don't even need a DB
    API available.

    Calls to context.execute() proxy to the environment's
    dot format block wholly.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_sync()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_sync()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
