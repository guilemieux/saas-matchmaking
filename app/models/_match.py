import sqlalchemy as sa
from sqlalchemy.orm import relationship

from app.database import Base


class Match(Base):
    __tablename__ = 'match'

    id = sa.Column('id', sa.Integer, primary_key=True)
    creation_time = sa.Column('time', sa.DateTime)

    players = relationship('Player', back_populates='match')
