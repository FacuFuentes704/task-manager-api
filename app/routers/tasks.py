from fastapi import APIRouter, Depends
from app.services.task_service import create_task, get_task_by_id, get_tasks, update_task, delete_task
from app.auth.auth import get_current_user
from app.database import get_db
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from sqlalchemy.orm import Session
from app.models.user import User

tasks_router = APIRouter(prefix="/tasks",
                         tags=["tasks"])

@tasks_router.get("/", response_model=list[TaskResponse])
def show_task(db: Session = Depends(get_db), get_user: User = Depends(get_current_user)):
    return get_tasks(db, get_user.id)

@tasks_router.get("/{task_id}", response_model=TaskResponse)
def show_by_id(task_id: int, db: Session = Depends(get_db), get_user: User = Depends(get_current_user)):
    return get_task_by_id(db, get_user.id, task_id)

@tasks_router.post("/", response_model=TaskResponse)
def create(task_data: TaskCreate, db: Session = Depends(get_db), get_user: User = Depends(get_current_user)):
    return create_task(db, get_user.id, task_data)

@tasks_router.patch("/{task_id}", response_model=TaskResponse)
def update(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db), get_user: User = Depends(get_current_user)):
    return update_task(db, get_user.id, task_data, task_id)

@tasks_router.delete("/{task_id}", status_code= 204)
def delete(task_id: int, db: Session = Depends(get_db), get_user: User = Depends(get_current_user)):
    delete_task(db, get_user.id, task_id)
