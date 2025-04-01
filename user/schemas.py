from datetime import datetime

from pydantic import BaseModel
from typing import Optional, List

# Request
class UserCreateRequest(BaseModel):
    login_id: str
    password: str
    username: str
    sex: bool
