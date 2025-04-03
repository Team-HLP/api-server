from pydantic import BaseModel

# Request
class GameCreateRequest(BaseModel):
    meteorite_broken_count: int
    play_time_seconds: int

# Response
class GameResponse(BaseModel):
    id: int
    user_id: int
    meteorite_broken_count: int
    play_time_seconds: int
