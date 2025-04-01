from sqlalchemy import Column, BIGINT, String, Boolean, func, DateTime
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from datebase import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True, comment="유저 고유 id")
    login_id = Column(String(20), nullable=False, unique=True, comment="유저 로그인 id")
    password = Column(MEDIUMTEXT, nullable=False, comment="`유저 비밀번호")
    username = Column(String(50), nullable=False, comment="유저 이름")
    sex = Column(Boolean, nullable=False, comment="성별")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
