from pydantic import BaseModel, Field
from typing import Optional
from app.schemas.task import TaskResponse

class CategoryCreate(BaseModel):
    name: str = Field(min_length=1)

class CategoryResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True

class CategoryUpdate(BaseModel):
    name: Optional[str] = None


class CategoryWithTasks(BaseModel):
    id: int
    name: str
    user_id: int
    tasks: list[TaskResponse] = []

    class Config:
        from_attributes = True