"""create match table

Revision ID: ea9e13c25f73
Revises: e593c2f4fa83
Create Date: 2021-09-11 15:38:59.175555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea9e13c25f73'
down_revision = 'e593c2f4fa83'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'match',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('time', sa.DateTime)
    )


def downgrade():
    op.drop_table('match')
