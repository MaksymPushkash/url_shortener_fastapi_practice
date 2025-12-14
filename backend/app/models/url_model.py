from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from backend.app.database.database import Base



class Urls(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    long_url = Column(String, nullable=False)
    short_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    clicks = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey("users.id"))



