from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datebase import get_db
from user.models import User
from game.models import Game
from game.schemas import *
from user.auth import get_current_user

router = APIRouter()

@router.post("", status_code=200)
def save_game(
    game_create: GameCreateRequest,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    new_game = Game(
        user_id=current_user.id,
        meteorite_broken_count=game_create.meteorite_broken_count,
        play_time_seconds=game_create.play_time_seconds
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return GameCreateResponse(
        id=new_game.id,
        user_id=current_user.id,
        meteorite_broken_count=new_game.meteorite_broken_count,
        play_time_seconds=new_game.play_time_seconds
    )
