"""add cost columns to queue

Revision ID: e593c2f4fa83
Revises: dc7e66758b4c
Create Date: 2021-09-05 21:27:08.205361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e593c2f4fa83'
down_revision = 'dc7e66758b4c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('queue', sa.Column('match_cost_function', sa.String(500)))
    op.add_column('queue', sa.Column('max_match_cost', sa.Numeric(precision=12, scale=6)))


def downgrade():
    op.drop_column('queue', 'max_match_cost')
    op.drop_column('queue', 'match_cost_function')
