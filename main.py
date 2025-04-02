from fastapi import FastAPI
from user.router import router as user_router
from user.models import User
from game.models import Game
from datebase import Base, engine

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])

Base.metadata.create_all(bind=engine)
