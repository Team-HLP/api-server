from fastapi import FastAPI
from datebase import Base, engine
from user.router import router as user_router
from user.models import User
from game.router import router as game_router
from game.models import Game

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(game_router, prefix="/game", tags=["game"])

Base.metadata.create_all(bind=engine)
