from fastapi import FastAPI
from app.database import Base, engine
from app.routers.users import users_router, auth_router
from app.routers.tasks import tasks_router
from app.models.user import User
from app.models.task import Task
from app.models.category import Category

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(tasks_router)