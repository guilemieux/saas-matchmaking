import fastapi

from app import dependencies
from app.routers import users

app = fastapi.FastAPI(dependencies=[fastapi.Depends(dependencies.get_session)])

app.include_router(users.router)
