import sqlalchemy as sa

from app.database import Base


class Queue(Base):
    __tablename__ = 'queue'

    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(200), nullable=False, index=True)
    match_cost_function = sa.Column('match_cost_function', sa.String(500))
    max_match_cost = sa.Column('max_match_cost', sa.Numeric(precision=12, scale=6))
