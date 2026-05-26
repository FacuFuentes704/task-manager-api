from fastapi import FastAPI
from app.database import Base, engine
from app.routers.users import users_router, auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)
app.include_router(auth_router)