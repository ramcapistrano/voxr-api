"""create_password_reset_table

Revision ID: e4afd2ea05aa
Revises: 3e0808cbe4a6
Create Date: 2017-11-01 17:12:10.922000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4afd2ea05aa'
down_revision = '3e0808cbe4a6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'password_resets',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('code', sa.String(4), nullable=False)
    )


def downgrade():
    pass
