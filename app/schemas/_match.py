from datetime import datetime

from pydantic import BaseModel, PositiveInt

from app.schemas import Player


class Match(BaseModel):
    id: PositiveInt
    creation_time: datetime
    players: list[Player]

    class Config:
        orm_mode = True
