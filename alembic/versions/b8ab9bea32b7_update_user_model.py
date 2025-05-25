"""update user model

Revision ID: b8ab9bea32b7
Revises: c4c5f0d0f5f0
Create Date: 2024-05-25 01:38:00.000000

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Enum

# revision identifiers, used by Alembic.
revision: str = 'b8ab9bea32b7'
down_revision: Union[str, None] = 'c4c5f0d0f5f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Crear el tipo ENUM primero
    gender_enum = sa.Enum('female', 'male', 'other', name='genderenum')
    gender_enum.create(op.get_bind())

    # Agregar las columnas
    op.add_column('users', sa.Column('code', sa.String(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('users', sa.Column('direction', sa.String(), nullable=True))
    op.add_column('users', sa.Column('birthdate', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('photo', sa.String(), nullable=True))
    op.add_column('users', sa.Column('last_access', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('gender', gender_enum, nullable=True))
    op.add_column('users', sa.Column('ci', sa.String(), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(), nullable=True))

def downgrade() -> None:
    # Eliminar las columnas
    op.drop_column('users', 'role')
    op.drop_column('users', 'ci')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'last_access')
    op.drop_column('users', 'photo')
    op.drop_column('users', 'birthdate')
    op.drop_column('users', 'direction')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'name')
    op.drop_column('users', 'code')
    
    # Eliminar el tipo ENUM
    sa.Enum(name='genderenum').drop(op.get_bind())