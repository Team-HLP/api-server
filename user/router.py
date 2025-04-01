from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datebase import get_db
from user.models import Users
from user.schemas import *
from user.auth import *

router = APIRouter()

@router.post("/register", status_code=201)
def register_user(user_create: UserCreateRequest, db: Session = Depends(get_db)):
    exist_user = db.query(Users).filter(Users.login_id == user_create.login_id).first()
    if exist_user:
        raise HTTPException(status_code=409, detail="이미 존재하는 사용자 ID입니다.")
    
    hashed_pw = hash_password(user_create.password)
    new_user = Users(
        login_id=user_create.login_id,
        password=hashed_pw,
        username=user_create.username,
        sex=user_create.sex
    )

    db.add(new_user)
    db.commit()
