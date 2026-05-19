from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Date
from datetime import datetime
from app.database import Base
from sqlalchemy import Enum 
import enum

class Status(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Priority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(Status), default=Status.pending)
    priority = Column(Enum(Priority), default=Priority.low)
    due_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)