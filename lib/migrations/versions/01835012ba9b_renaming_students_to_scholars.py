"""renaming students to scholars

Revision ID: 01835012ba9b
Revises: 791279dd0760
Create Date: 2023-12-05 20:47:45.389424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01835012ba9b'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
