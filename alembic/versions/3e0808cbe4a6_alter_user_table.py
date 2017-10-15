"""alter_user_table

Revision ID: 3e0808cbe4a6
Revises: 74f56008a800
Create Date: 2017-10-15 02:11:12.611000

"""
from alembic import op
from sqlalchemy.dialects.mysql import DOUBLE
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e0808cbe4a6'
down_revision = '74f56008a800'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('records', 'neutrality', type_=DOUBLE)
    op.alter_column('records', 'happiness', type_=DOUBLE)
    op.alter_column('records', 'sadness', type_=DOUBLE)
    op.alter_column('records', 'anger', type_=DOUBLE)
    op.alter_column('records', 'fear', type_=DOUBLE)


def downgrade():
    pass
