"""create queue table

Revision ID: dc7e66758b4c
Revises: 
Create Date: 2021-09-04 18:02:33.883615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc7e66758b4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'queue',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(200), nullable=False, index=True),
    )


def downgrade():
    op.drop_table('queue')
