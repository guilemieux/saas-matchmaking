from sqlalchemy.orm import Session

from app import models, schemas


def get_items(session: Session, skip: int = 0, limit: int = 100) -> list[models.Item]:
    return session.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(session: Session, item: schemas.ItemCreate, user_id: int) -> models.Item:
    db_item = models.Item(**item.dict(), owner_id=user_id)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item