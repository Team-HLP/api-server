import bcrypt
from jose import jwt
from config import *
from datebase import *
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from jose import JWTError
from sqlalchemy.orm import Session
from user.models import User

oauth2_scheme = APIKeyHeader(name="Authorization", auto_error=True)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_mysql)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="인증 정보가 올바르지 않습니다.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_sub": False})
        id: str = payload.get("sub")
        if id is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception

    db_user = db.query(User).filter(User.id == id).first()
    if db_user is None:
        raise credentials_exception

    return db_user
