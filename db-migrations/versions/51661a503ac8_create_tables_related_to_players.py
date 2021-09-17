"""create tables related to players

Revision ID: 51661a503ac8
Revises: ea9e13c25f73
Create Date: 2021-09-16 21:20:36.638640

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import func


# revision identifiers, used by Alembic.
revision = '51661a503ac8'
down_revision = 'ea9e13c25f73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'player',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('queue_id', sa.Integer, sa.ForeignKey('queue.id'), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('status', sa.String(50), nullable=False),
        sa.Column('match_id', sa.Integer, sa.ForeignKey('match.id')),
        sa.Column('join_time', sa.DateTime, server_default=func.now()),
        sa.Column('attributes', sa.JSON)
    )


def downgrade():
    op.drop_table('player')
