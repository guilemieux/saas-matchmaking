from typing import Optional

from sqlalchemy.orm import Session

from app import schemas, models


async def create_queue(session: Session, queue: schemas.QueueCreate) -> models.Queue:
    db_queue = models.Queue(name=queue.name)
    session.add(db_queue)
    session.commit()
    session.refresh(db_queue)
    return db_queue


async def get_queues(session: Session, skip: int = 0, limit: int = 100) -> list[models.Queue]:
    return session.query(models.Queue).offset(skip).limit(limit).all()


async def get_queue(session: Session, queue_id: int) -> Optional[models.Queue]:
    return session.query(models.Queue).filter(models.Queue.id == queue_id).first()
