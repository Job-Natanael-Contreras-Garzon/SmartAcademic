"""create initial tables based on models

Revision ID: 80e5c5a3d5d0
Revises: b8ab9bea32b7
Create Date: 2025-05-26 00:53:17.705555
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = '80e5c5a3d5d0'
down_revision: Union[str, None] = 'b8ab9bea32b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def create_enum_if_not_exists(enum_name, values):
    """Create ENUM type if it doesn't exist."""
    op.execute(f"""
        DO $$
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = '{enum_name}') THEN
                CREATE TYPE {enum_name} AS ENUM {values};
            END IF;
        END$$;
    """)

def upgrade() -> None:
    """Upgrade schema."""
    # Crear ENUMs de forma segura
    create_enum_if_not_exists('genderenum', "('female', 'male', 'other')")
    create_enum_if_not_exists('roleenum', "('student', 'teacher', 'patterns', 'administrator')")
    create_enum_if_not_exists('gradeenum', "('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'kinder', 'prekinder')")
    create_enum_if_not_exists('levelenum', "('initial', 'primary', 'secondary')")
    create_enum_if_not_exists('tuitionstatusenum', "('paid', 'pending', 'overdue')")

    # Definir tipos ENUM para uso en las tablas
    gender_enum = postgresql.ENUM('female', 'male', 'other', name='genderenum', create_type=False)
    role_enum = postgresql.ENUM('student', 'teacher', 'patterns', 'administrator', name='roleenum', create_type=False)
    grade_enum = postgresql.ENUM('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'kinder', 'prekinder', name='gradeenum', create_type=False)
    level_enum = postgresql.ENUM('initial', 'primary', 'secondary', name='levelenum', create_type=False)
    status_enum = postgresql.ENUM('paid', 'pending', 'overdue', name='tuitionstatusenum', create_type=False)

    # Crear los tipos ENUM en la base de datos
    for enum in [gender_enum, role_enum, grade_enum, level_enum, status_enum]:
        enum.create(op.get_bind(), checkfirst=True)

    # Crear tablas
    op.create_table('groups',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('grade', grade_enum, nullable=False),
        sa.Column('level', level_enum, nullable=False),
        sa.Column('group', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_groups_id'), 'groups', ['id'], unique=False)

    # ... (resto de create_table sin cambios)

    # Modificar la tabla users existente
    op.alter_column('users', 'code',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('users', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('users', 'last_name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('users', 'email',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    
    # Crear columnas con ENUM
    op.alter_column('users', 'gender',
                    existing_type=sa.VARCHAR(),
                    type_=gender_enum,
                    nullable=False,
                    postgresql_using="gender::genderenum")
    op.alter_column('users', 'role',
                    existing_type=sa.VARCHAR(),
                    type_=role_enum,
                    nullable=False,
                    postgresql_using="role::roleenum")

    # Resto de alteraciones a users
    op.alter_column('users', 'ci',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_index(op.f('ix_users_code'), 'users', ['code'], unique=True)
    op.create_unique_constraint(None, 'users', ['ci'])
    
    # Eliminar columnas obsoletas
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'username')
    op.drop_column('users', 'hashed_password')
    op.drop_column('users', 'created_at')

def downgrade() -> None:
    """Downgrade schema."""
    # Primero restaurar columnas de users
    op.add_column('users', sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), 
                                   server_default=sa.text('now()'), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), 
                                   autoincrement=False, nullable=True))

    # Revertir cambios en users
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_index(op.f('ix_users_code'), table_name='users')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    
    # Convertir ENUMs a VARCHAR
    op.alter_column('users', 'role',
                    existing_type=role_enum,
                    type_=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('users', 'gender',
                    existing_type=gender_enum,
                    type_=sa.VARCHAR(),
                    nullable=True)

    # Eliminar tablas en orden inverso
    for table in ['total_notes', 'subcriteria_notes', 'student_tutors', 
                 'student_tuitions', 'student_subject', 'user_group', 
                 'subcriteria', 'students', 'tuitions', 'subjects', 
                 'periods', 'main_approaches', 'groups']:
        op.drop_table(table)

    # Eliminar tipos ENUM
    for enum_name in ['genderenum', 'roleenum', 'gradeenum', 'levelenum', 'tuitionstatusenum']:
        op.execute(f'DROP TYPE IF EXISTS {enum_name}')