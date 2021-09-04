import sqlalchemy as sa

import app.database as db

class Item(db.Base):
    __tablename__ = "item"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String, index=True)
    description = sa.Column(sa.String, index=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))

    owner = sa.orm.relationship("User", back_populates="items")
