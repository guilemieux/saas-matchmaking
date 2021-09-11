import sqlalchemy as sa

from app.database import Base


class Ticket(Base):
    __tablename__ = 'ticket'

    id = sa.Column('id', sa.Integer, primary_key=True)
    match_id = sa.Column('match_id', sa.Integer, sa.ForeignKey('match.id'), nullable=False)
    creation_time = sa.Column('creation_time', sa.DateTime)
    status = sa.Column('status', sa.String(50), nullable=False)
