from typing import List
from fastapi import APIRouter, HTTPException, status
from backend.app.api.v1.user import user_dependency
from backend.app.services.url_service import create_url, get_url_by_short, increment_clicks, get_urls_by_user
from backend.app.dependencies import db_dependency
from backend.app.schemas.url_schema import UrlCreate, UrlInfo



router = APIRouter(prefix="/url", tags=["url"])




@router.post("/shorten")
def shorten_url(url: UrlCreate, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

    db_url = create_url(db, str(url.long_url), user_id=user.get("user_id"))
    return db_url


@router.get("/get-my-urls", response_model=List[UrlInfo])
def get_my_urls(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")

    user_id = user.get("user_id")
    urls = get_urls_by_user(db, user_id=user_id)
    return urls



@router.get("/{short_url}")
def redirect_url(short_url: str, user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")


    db_url = get_url_by_short(db, short_url)

    if db_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")

    increment_clicks(db, db_url)
    return {"long_url": db_url.long_url}



