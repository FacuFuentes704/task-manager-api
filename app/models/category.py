from app.database import Base
from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    tasks = relationship("Task", back_populates="category")