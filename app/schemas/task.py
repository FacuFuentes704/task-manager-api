from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True