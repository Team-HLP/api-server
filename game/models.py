from sqlalchemy import Column, BIGINT, func, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datebase import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True, comment="게임 고유 id")
    user_id = Column(BIGINT, ForeignKey("users.id"), nullable=False, comment="유저 고유 id")
    meteorite_broken_count = Column(BIGINT, nullable=False, comment="운석 파괴 횟수")
    play_time_seconds = Column(Integer, nullable=False, comment="플레이 타임 (초 단위)")
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="games")
