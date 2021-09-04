"""Create initial tables

Revision ID: c7e394078da5
Revises: 
Create Date: 2021-09-03 23:33:19.921605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7e394078da5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True),
        sa.Column('hashed_password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True),
    )
    op.create_table(
        'item',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('description', sa.String, index=True),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey("user.id")),
    )




def downgrade():
    op.drop_table('item')
    op.drop_table('user')
