from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datebase import get_mysql
from user.models import User
from game.models import Game
from game.schemas import *
from user.auth import get_current_user

router = APIRouter()

@router.post("", status_code=200)
def save_game(
    game_create: GameCreateRequest,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_mysql)
):
    new_game = Game(
        user_id=current_user.id,
        meteorite_broken_count=game_create.meteorite_broken_count,
        play_time_seconds=game_create.play_time_seconds,
        blink_eye_count=game_create.blink_eye_count,
        avg_pupil_size=game_create.avg_pupil_size
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return GameResponse(
        id=new_game.id,
        user_id=current_user.id,
        meteorite_broken_count=new_game.meteorite_broken_count,
        play_time_seconds=new_game.play_time_seconds,
        blink_eye_count=game_create.blink_eye_count,
        avg_pupil_size=game_create.avg_pupil_size
    )

@router.get("", response_model=list[GameResponse], status_code=200)
def get_games(
    # current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_mysql)
):
    return db.query(Game).filter(Game.user_id == 2).all()

@router.get("/{gameId}", response_model=GameResponse, status_code=200)
def get_game(
    game_id: int,
    current_user: User = Depends(get_current_user), 
    db: Session = Depends(get_mysql)
):
    game = db.query(Game).filter(Game.id == game_id, Game.user_id == current_user.id).first()
    if not game:
        raise HTTPException(status_code=404, detail="게임을 찾을 수 없습니다.")
    
    return game
