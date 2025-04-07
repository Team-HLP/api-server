from pydantic import BaseModel, Field
from typing import List

class GazeData(BaseModel):
    timestamp: float = Field(..., description="Unity의 Time.time 값 (초 단위)")
    x: float = Field(..., description="Gaze origin X 좌표")
    y: float = Field(..., description="Gaze origin Y 좌표")
    z: float = Field(..., description="Gaze origin Z 좌표")

class GazePacket(BaseModel):
    user_id: int = Field(..., description="유저 ID")
    game_id: int = Field(..., description="게임 ID")
    data: List[GazeData]
