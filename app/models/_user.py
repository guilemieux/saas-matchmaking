import sqlalchemy as sa

import app.database as db

class User(db.Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    email = sa.Column(sa.String, unique=True, index=True)
    hashed_password = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean, default=True)

    items = sa.orm.relationship("Item", back_populates="owner")
