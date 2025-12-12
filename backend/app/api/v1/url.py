from fastapi import APIRouter, HTTPException, status
from backend.app.services.url_service import create_url, get_url_by_short, increment_clicks
from backend.app.dependencies import db_dependency
from backend.app.schemas.url_schema import UrlCreate



router = APIRouter(prefix="/url", tags=["url"])





@router.post("/shorten")
def shorten_url(url: UrlCreate, db: db_dependency):
    db_url = create_url(db, str(url.long_url))
    return db_url


@router.get("/{short_url}")
def redirect_url(short_url: str, db: db_dependency):
    db_url = get_url_by_short(db, short_url)

    if db_url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")

    increment_clicks(db, db_url)
    return {"long_url": db_url.long_url}