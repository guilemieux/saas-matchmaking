from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr, PositiveInt


class PlayerStatusEnum(str, Enum):
    waiting = 'WAITING'
    matched = 'MATCHED'
    canceled = 'CANCELED'


class PlayerCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    queue_id: PositiveInt
    attributes: dict[str, float]


class Player(BaseModel):
    id: PositiveInt
    name: constr(min_length=1, max_length=100)
    queue_id: PositiveInt
    status: PlayerStatusEnum
    join_time: Optional[datetime]
    match_id: Optional[PositiveInt]
    attributes: dict[str, float]

    class Config:
        orm_mode = True
