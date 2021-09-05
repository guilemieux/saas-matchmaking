from pydantic import BaseModel, constr, PositiveInt


class QueueCreate(BaseModel):
    name: constr(max_length=200)


class Queue(BaseModel):
    id: PositiveInt
    name: constr(max_length=200)

    class Config:
        orm_mode = True
