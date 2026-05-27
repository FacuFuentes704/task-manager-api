from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from sqlalchemy.orm import Session
from fastapi import HTTPException

def create_task(user_id: int, task_data: TaskCreate, db: Session):
    new_task = Task(**task_data.model_dump(), user_id = user_id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(user_id: int, db: Session):
    resultado = db.query(Task).filter(Task.user_id == user_id).all()
    return resultado

def get_task_by_id(user_id: int, task_id : int, db: Session):
    resultado = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron tareas")
    return resultado

def update_task(user_id: int, task_id: int, db: Session, task_data: TaskUpdate):
    resultado = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron resultados")
    datos = task_data.model_dump(exclude_unset=True)
    for campo, valor in datos.items():
        setattr (resultado, campo, valor)
    db.commit()
    db.refresh(resultado)
    return resultado

def delete_task(user_id: int, task_id: int, db: Session):
    resultado = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron resultados")
    db.delete(resultado)
    db.commit()
    return

    
