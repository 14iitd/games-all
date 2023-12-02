from typing import List, Optional
from pydantic import BaseModel

class User(BaseModel):
    id : str
    username: str
    email: str
    full_name: str
    bio: Optional[str] = None
    profile_picture: Optional[str] = None
    device_id: str

class Question(BaseModel):
    id: str
    content: str
    options: List
class QuestionResponse(BaseModel):
    id: str
    user_id: str
    user_option: object

