from datetime import datetime

from pydantic import BaseModel, PositiveInt


class Match(BaseModel):
    id: PositiveInt
    creation_time: datetime

    class Config:
        orm_mode = True
