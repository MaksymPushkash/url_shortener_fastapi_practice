
from fastapi import HTTPException, APIRouter, status
from backend.app.dependencies import db_dependency, user_dependency
from backend.app.models.user_model import Users
from backend.app.schemas.user_schema import CreateUserRequest
from backend.app.security.user_auth import bcrypt_context

router = APIRouter(prefix="/user", tags=["user"])



@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

    return db.query(user).filter(Users.id == user.get("id")).first()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(email=create_user_request.email,
                              username=create_user_request.username,
                              role=create_user_request.role,
                              hashed_password=bcrypt_context.hash(create_user_request.password),
                              is_active=True)
    db.add(create_user_model)
    db.commit()

