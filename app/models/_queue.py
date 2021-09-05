import sqlalchemy as sa

from app.database import Base


class Queue(Base):
    __tablename__ = 'queue'

    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(200), nullable=False, index=True)
