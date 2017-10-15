"""alter user table

Revision ID: 3d66620f6a58
Revises: 863e2e531ff0
Create Date: 2017-10-13 15:47:00.267000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d66620f6a58'
down_revision = '863e2e531ff0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint("uq_user_username", 'users', ["username"])


def downgrade():
    pass
