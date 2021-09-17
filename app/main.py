import uvicorn
from fastapi import FastAPI, Depends

from app.dependencies import get_session
from app.routers import queues, matches, players

app = FastAPI(dependencies=[Depends(get_session)])

app.include_router(queues.router)
app.include_router(matches.router)
app.include_router(players.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
