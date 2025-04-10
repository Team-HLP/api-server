from pydantic import BaseModel
from datetime import datetime

# Request
class GameCreateRequest(BaseModel):
    meteorite_broken_count: int
    play_time_seconds: int
    blink_eye_count: int
    avg_pupil_size: float

# Response
class GameResponse(BaseModel):
    id: int
    user_id: int
    meteorite_broken_count: int
    play_time_seconds: int
    blink_eye_count: int
    avg_left_eye_pupil_size: float
    avg_right_eye_pupil_size: float
    created_at: datetime
