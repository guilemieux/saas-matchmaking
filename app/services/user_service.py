from typing import Optional
from sqlalchemy.orm import Session

from app import models, schemas


def get_user(session: Session, id: int) -> Optional[models.User]:
    return session.query(models.User).filter(models.User.id == id).first()


def get_user_by_email(session: Session, email: str) -> Optional[models.User]:
    return session.query(models.User).filter(models.User.email == email).first()


def get_users(session: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return session.query(models.User).offset(skip).limit(limit).all()


def create_user(session: Session, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
