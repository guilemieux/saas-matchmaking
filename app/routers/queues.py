from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_session
from app.services import queue_service

router = APIRouter(
    tags=['Queues'],
    responses={404: {'description': 'Not Found'}}
)


@router.post(path='/queues', response_model=schemas.Queue)
async def create_queue(queue: schemas.QueueCreate, session: Session = Depends(get_session)):
    return await queue_service.create_queue(session, queue)


@router.get(path='/queues', response_model=list[schemas.Queue])
async def get_queues(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return await queue_service.get_queues(session, skip, limit)


@router.get(path='/queues/{queue_id}', response_model=schemas.Queue)
async def get_queue(queue_id: int, session: Session = Depends(get_session)):
    db_queue = await queue_service.get_queue(session, queue_id)
    if db_queue is None:
        raise HTTPException(status_code=404, detail="Queue not found")
    return db_queue
