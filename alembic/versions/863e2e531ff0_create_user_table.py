"""create user table

Revision ID: 863e2e531ff0
Revises: 
Create Date: 2017-10-13 11:07:44.066000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '863e2e531ff0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False)
    )

    op.create_table(
        'records',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('neutrality', sa.String(50), nullable=False),
        sa.Column('happiness', sa.String(50), nullable=False),
        sa.Column('sadness', sa.String(50), nullable=False),
        sa.Column('anger', sa.String(50), nullable=False),
        sa.Column('fear', sa.String(50), nullable=False),
        sa.Column('file_path', sa.String(100), nullable=False),
        sa.Column('date_created', sa.TIMESTAMP, nullable=False),
    )


def downgrade():
    pass
