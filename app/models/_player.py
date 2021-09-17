import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import relationship

from app.database import Base


class Player(Base):
    __tablename__ = 'player'

    id = sa.Column('id', sa.Integer, primary_key=True)
    name = sa.Column('name', sa.String(100), nullable=False)
    queue_id = sa.Column('queue_id', sa.Integer, sa.ForeignKey('queue.id'), nullable=False)
    status = sa.Column('status', sa.String(50), nullable=False)
    match_id = sa.Column('match_id', sa.Integer, sa.ForeignKey('match.id'))
    join_time = sa.Column('join_time', sa.DateTime, server_default=func.now())
    attributes = sa.Column('attributes', sa.JSON)

    queue = relationship('Queue', back_populates='players')
    match = relationship('Match', back_populates='players')
