import sqlalchemy as sa

from app.database import Base

class Player(Base):
    __tablename__ = 'player'

