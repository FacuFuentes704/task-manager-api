from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserLogin, UserResponse, TokenResponse, UserUpdate
from app.services.user_service import register_user, login_user, get_profile, update_user, delete_user
from app.database import get_db
from app.models.user import User
from app.auth.auth import get_current_user

users_router = APIRouter(prefix="/users",
                   tags=["users"])

auth_router = APIRouter(prefix="/auth",
                        tags=["auth"])


@users_router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user_data)

@auth_router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user_data)

@users_router.get("/", response_model=UserResponse)
def show_profile(db: Session = Depends(get_db), user_data: User = Depends(get_current_user)):
    return get_profile(db, user_data.id)

@users_router.patch("/", response_model=UserResponse)
def update(user_data: UserUpdate, db: Session = Depends(get_db), user_id: User = Depends(get_current_user)):
    return update_user(db, user_id.id, user_data)

@users_router.delete("/", status_code=204)
def delete(db: Session = Depends(get_db), user_id: User = Depends(get_current_user)):
    return delete_user(db, user_id.id)

