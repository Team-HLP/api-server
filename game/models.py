from sqlalchemy import Column, BIGINT, func, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from datebase import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True, comment="게임 고유 id")
    user_id = Column(BIGINT, ForeignKey("users.id"), nullable=False, comment="유저 고유 id")
    meteorite_broken_count = Column(BIGINT, nullable=False, comment="운석 파괴 횟수")
    play_time_seconds = Column(Integer, nullable=False, comment="플레이 타임 (초 단위)")
    blink_eye_count = Column(Integer, nullable=False, comment="눈 깜빡임 횟수")
    avg_pupil_size = Column(Float, nullable=False, comment="평균 동공 크기")
    created_at = Column(DateTime, nullable=False, default=func.now())

    user = relationship("User", back_populates="games")
