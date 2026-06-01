from app.models.category import Category
from sqlalchemy.orm import Session
from app.schemas.category import CategoryCreate, CategoryUpdate
from fastapi import HTTPException

def create_category(db: Session, user_id: int, category_data: CategoryCreate):
    new_category = Category(**category_data.model_dump(), user_id = user_id)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_categories(db: Session, user_id: int):
    resultado = db.query(Category).filter(Category.user_id == user_id).all()
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontraron categorias asociadas al usuario")
    return resultado

def update_category(db: Session, user_id:int, category_id: int, category_data: CategoryUpdate):
    resultado = db.query(Category).filter(Category.id == category_id, Category.user_id == user_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="No se encontro una categoria")
    datos = category_data.model_dump(exclude_unset=True)
    for campo, valor in datos.items():
        setattr(resultado, campo, valor)
    db.commit()
    db.refresh(resultado)
    return resultado

def delete_category(db: Session, user_id: int, category_id: int):
    resultado = db.query(Category).filter(Category.id == category_id, Category.user_id == user_id).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    db.delete(resultado)
    db.commit()
    return

def get_category_with_tasks(db: Session, user_id: int, category_id: int):
    respuesta = db.query(Category).filter(Category.id == category_id, Category.user_id == user_id).first()
    if not respuesta:
        raise HTTPException(status_code=404, detail="No se encontraron categorias")
    return respuesta
    
    