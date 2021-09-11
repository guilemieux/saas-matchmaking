from datetime import datetime

from pydantic import BaseModel, PositiveInt


class Match(BaseModel):
    id: PositiveInt
    time: datetime
