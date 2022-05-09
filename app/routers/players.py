from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.dependencies import get_session
from app.services.player_service import PlayerService

router = APIRouter(
    tags=['Players'],
)


@router.post(path='/players', response_model=schemas.Player)
async def create_player(player: schemas.PlayerCreate, session: Session = Depends(get_session)):
    return PlayerService(session).add(player)


@router.get(path='/players/{player_id}', response_model=schemas.Player)
async def get_player(player_id: int, session: Session = Depends(get_session)):
    player_service = PlayerService(session)
    db_player = player_service.get(player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return db_player
