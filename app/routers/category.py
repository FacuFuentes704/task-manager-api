from fastapi import APIRouter, Depends
from app.services.category_service import create_category, get_categories, update_category, delete_category, get_category_with_tasks
from app.auth.auth import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate, CategoryWithTasks
from app.models.user import User

category_router = APIRouter(prefix="/categories",
                            tags=["categories"])

@category_router.get("/", response_model=list[CategoryResponse])
def show_categories(db: Session = Depends(get_db), user_data: User = Depends(get_current_user)):
    return get_categories(db, user_data.id)

@category_router.post("/", response_model=CategoryResponse)
def create(category_data: CategoryCreate, db: Session = Depends(get_db), user_data: User = Depends(get_current_user)):
    return create_category(db, user_data.id, category_data)

@category_router.patch("/{category_id}", response_model=CategoryResponse)
def update(category_data: CategoryUpdate, category_id: int, db: Session = Depends(get_db), user_data: User = Depends(get_current_user)):
    return update_category(db, user_data.id, category_id, category_data)

@category_router.delete("/{category_id}", status_code=204)
def delete(category_id: int, db: Session = Depends(get_db), user_data: User = Depends(get_current_user)):
    return delete_category(db, user_data.id, category_id)

@category_router.get("/{category_id}", response_model=CategoryWithTasks)
def show_tasks(category_id: int, db: Session = Depends(get_db), user_data: User = Depends(get_current_user)):
    return get_category_with_tasks(db, user_data.id, category_id)