from http.client import HTTPException
from typing import Annotated

from fastapi.openapi.utils import status_code_ranges
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, status
import os
from dotenv import load_dotenv
from backend.app.dependencies import db_dependency
from passlib.context import CryptContext
from jose import jwt, JWTError





router = APIRouter(prefix="/auth", tags=["auth"])



bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


