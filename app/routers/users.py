from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from app.dependencies import get_session
from app import schemas
from app.services import user_service


router = APIRouter()


@router.post("/users", response_model=schemas.User, tags=['users'])
def create_user(user: schemas.UserCreate, session: Session = Depends(get_session)):
    user = user_service.get_user_by_email(session, user.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(session, user)


@router.get("/users", response_model=list[schemas.User], tags=['users'])
def read_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users = user_service.get_users(session, skip=skip, limit=limit)
    return users
