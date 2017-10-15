"""alter_user_table

Revision ID: c3a56e94bdb2
Revises: 3d66620f6a58
Create Date: 2017-10-14 13:04:54.907000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3a56e94bdb2'
down_revision = '3d66620f6a58'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users',
        sa.Column('email', sa.String(50), nullable=True)
    )


def downgrade():
    pass
