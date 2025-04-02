from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datebase import get_db
from user.models import User
from game.models import Game
from game.schemas import *

router = APIRouter()

@router.post("", status_code=200)
def save_game(game_create: GameCreateRequest, db: Session = Depends(get_db)):
    exist_user = db.query(User).filter(User.id == game_create.user_id).first()
    if not exist_user:
        raise HTTPException(status_code=400, detail="존재하지 않는 사용자입니다.")
    
    new_game = Game(
        user_id=game_create.user_id,
        meteorite_broken_count=game_create.meteorite_broken_count,
        play_time_seconds=game_create.play_time_seconds
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return GameCreateResponse(
        id=new_game.id,
        user_id=new_game.user_id,
        meteorite_broken_count=new_game.meteorite_broken_count,
        play_time_seconds=new_game.play_time_seconds
    )
