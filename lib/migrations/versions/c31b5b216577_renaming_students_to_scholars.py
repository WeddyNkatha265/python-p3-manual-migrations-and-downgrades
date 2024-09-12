"""Renaming students to scholars

Revision ID: c31b5b216577
Revises: 791279dd0760
Create Date: 2024-09-13 00:21:21.197944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c31b5b216577'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
