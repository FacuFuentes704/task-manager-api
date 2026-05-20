from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from app.models.task import Status, Priority


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    description: Optional[str] = None
    status: Optional[Status] = Status.pending
    priority: Optional[Priority] = Priority.low
    due_date: Optional[date] = None
    category_id: Optional[int] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: Status
    priority: Priority
    due_date: Optional[date] = None
    category_id: Optional[int] = None
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[Status] = None
    priority: Optional[Priority] = None
    due_date: Optional[date] = None
    category_id: Optional[int] = None
