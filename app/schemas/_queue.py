from typing import Optional

from lark.exceptions import LarkError
from pydantic import BaseModel, constr, PositiveInt, confloat, validator

from app.services.mcf_parser import mcf_parser


class QueueCreate(BaseModel):
    name: constr(min_length=1, max_length=200)
    match_cost_function: Optional[constr(max_length=500)] = None
    max_match_cost: Optional[confloat(ge=0, lt=1E6)] = None

    @validator('match_cost_function')
    def match_cost_function_must_be_parsable(cls, mcf: str):
        if mcf is None:
            return mcf
        try:
            mcf_parser.parse(mcf)
        except LarkError as err:
            raise ValueError('Unable to parse match cost function.') from err
        return mcf

    @validator('max_match_cost')
    def match_cost_must_be_none_if_mcf_is_none(cls, mmc: Optional[float], values: dict[str, any]):
        if mmc is not None and values['match_cost_function'] is None:
            raise ValueError('max_match_cost can only be set if the queue has a match_cost_function.')
        return mmc


class Queue(BaseModel):
    id: PositiveInt
    name: constr(max_length=200)
    match_cost_function: Optional[constr(max_length=500)] = None
    max_match_cost: Optional[confloat(ge=0, lt=1E6)] = None

    class Config:
        orm_mode = True
