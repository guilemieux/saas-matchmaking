from fastapi import APIRouter, Depends
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
