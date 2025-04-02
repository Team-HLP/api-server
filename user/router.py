from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datebase import get_db
from user.models import User
from user.schemas import *
from user.auth import *

router = APIRouter()

@router.post("/register", status_code=201)
def register_user(user_create: UserCreateRequest, db: Session = Depends(get_db)):
    exist_user = db.query(User).filter(User.login_id == user_create.login_id).first()
    if exist_user:
        raise HTTPException(status_code=409, detail="이미 존재하는 사용자 ID입니다.")
    
    hashed_pw = hash_password(user_create.password)
    new_user = User(
        login_id=user_create.login_id,
        password=hashed_pw,
        username=user_create.username,
        sex=user_create.sex
    )

    db.add(new_user)
    db.commit()

@router.post("/login", status_code=200, response_model=UserLoginResponse)
def login_user(user_login: UserLoginRequest, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.login_id == user_login.login_id).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="존재하지 않는 유저입니다")
    if not verify_password(user_login.password, db_user.password):
        raise HTTPException(status_code=400, detail="비밀번호가 올바르지 않습니다.")
    
    access_token = create_access_token({"sub": db_user.id})

    return {"access_token": access_token}
