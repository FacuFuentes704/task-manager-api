from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse
from app.services.user_service import register_user, login_user

users_router = APIRouter(prefix="/users",
                   tags=["users"])

auth_router = APIRouter(prefix="/auth",
                        tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@users_router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_data)

@auth_router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user_data)
