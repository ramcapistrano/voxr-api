"""alter_user_table

Revision ID: ba8e21d86b95
Revises: c3a56e94bdb2
Create Date: 2017-10-15 00:39:40.069000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba8e21d86b95'
down_revision = 'c3a56e94bdb2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint("uq_user_email", 'users', ["email"])


def downgrade():
    pass
