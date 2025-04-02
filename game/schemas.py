from pydantic import BaseModel

# Request
class GameCreateRequest(BaseModel):
    user_id: int
    meteorite_broken_count: int
    play_time_seconds: int

# Response
class GameCreateResponse(BaseModel):
    id: int
    user_id: int
    meteorite_broken_count: int
    play_time_seconds: int
