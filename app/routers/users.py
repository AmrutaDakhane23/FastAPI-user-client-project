from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.auth import hash_password

router = APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(user.password)

    new_user = models.User(
        name = user.name,
        email = user.email,
        password = hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()