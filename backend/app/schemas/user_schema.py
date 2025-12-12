from pydantic import BaseModel


class UserVerification(BaseModel):
    password: str


class CreateUserRequest(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str


