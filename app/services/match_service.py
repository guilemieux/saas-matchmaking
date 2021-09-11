from typing import Optional

from sqlalchemy.orm import Session

from app import models


async def get_matches(session: Session, skip: int = 0, limit: int = 100) -> list[models.Match]:
    return session.query(models.Match).offset(skip).limit(limit).all()


async def get_match(session: Session, match_id: int) -> Optional[models.Match]:
    return session.query(models.Match).filter(models.Match.id == match_id).first()
