from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.auth import verify_password, create_token

router =  APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()

@router.post("/login")
def login(email: str, password : str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException (status_code=400, detail="Invalid credentials")
    
    token = create_token({"user_id":user.id})

    return {"access_token":token}
