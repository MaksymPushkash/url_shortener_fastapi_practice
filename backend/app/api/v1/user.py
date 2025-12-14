
from fastapi import HTTPException, APIRouter, status, Depends
from typing import Annotated
from backend.app.dependencies import db_dependency
from backend.app.models.user_model import Users
from backend.app.security.user_auth import get_current_user

router = APIRouter(prefix="/user", tags=["user"])

user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

    return db.query(Users).filter(Users.id == user.get("user_id")).first()




