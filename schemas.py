from pydantic import BaseModel,Field,field_validator
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str = Field(..., min_length=8)

    
    @field_validator('password')
    @classmethod
    def password_check(cls, v: str):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one number')
        if not any(char.isalpha() for char in v):
            raise ValueError('Password must contain at least one letter')
        return v

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config:
        from_attributes = True

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user_id: int
class User(BaseModel):
    username: str
    class Config:
        orm_mode = True

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user_id: User
    class Config:
        orm_mode = True

