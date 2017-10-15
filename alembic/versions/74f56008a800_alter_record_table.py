"""alter_record_table

Revision ID: 74f56008a800
Revises: ba8e21d86b95
Create Date: 2017-10-15 01:29:37.732000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f56008a800'
down_revision = 'ba8e21d86b95'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'records',
        sa.Column('date_deleted', sa.TIMESTAMP, nullable=True)
    )


def downgrade():
    pass
