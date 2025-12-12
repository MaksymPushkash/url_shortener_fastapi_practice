from pydantic import BaseModel, HttpUrl


class UrlCreate(BaseModel):
    long_url: HttpUrl

class UrlInfo(BaseModel):
    long_url: str
    short_url: str
    clicks: int

    class Config:
        from_attributes = True
