# here is business logic

import random, string
from backend.app.models.url_model import Urls
from sqlalchemy.orm import Session


def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_url(db: Session, long_url: str):
    short_url = generate_short_url()
    db_url = Urls(long_url=long_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_url_by_short(db: Session, short_url: str):
    return db.query(Urls).filter(Urls.short_url == short_url).first()


def increment_clicks(db: Session, url):
    url.clicks += 1
    db.commit()
    db.refresh(url)
    return url


