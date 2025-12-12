from fastapi import FastAPI
from backend.app.api.v1 import url, user
from backend.app.models.url_model import Base
from backend.app.database.database import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}

app.include_router(url.router)
app.include_router(user.router)







