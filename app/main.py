#Run: fastapi dev ./app/main.py
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

#models.Base.metadata.create_all(bind=engine) - I use Alembic now

app = FastAPI()

#conn = psycopg.connect("dbname=fastapi user=postgres password=password ", row_factory=dict_row)
#cur = conn.cursor()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hellow world"}
