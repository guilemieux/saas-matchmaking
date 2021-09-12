from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_session
from app.services import match_service

router = APIRouter(
    tags=['Matches'],
    responses={404: {'description': 'Not Found'}}
)


@router.get(path='/matches', response_model=list[schemas.Match])
async def get_matches(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return await match_service.get_matches(session, skip, limit)


@router.get(path='/matches/{match_id}', response_model=schemas.Match)
async def get_match(match_id: int, session: Session = Depends(get_session)):
    db_match = await match_service.get_match(session, match_id)
    if db_match is None:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match
