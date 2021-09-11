from typing import Optional

from pydantic import BaseModel, constr, PositiveInt, confloat


class QueueCreate(BaseModel):
    name: constr(max_length=200)
    match_cost_function: Optional[constr(max_length=500)] = None
    max_match_cost: Optional[confloat(ge=0, lt=1E6)] = None


class Queue(BaseModel):
    id: PositiveInt
    name: constr(max_length=200)
    match_cost_function: Optional[constr(max_length=500)] = None
    max_match_cost: Optional[confloat(ge=0, lt=1E6)] = None

    class Config:
        orm_mode = True
