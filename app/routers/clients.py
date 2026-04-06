from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.deps import get_db
from app import models, schemas
from app.auth import get_current_user

router = APIRouter(prefix="/clients")

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_client(
    client: schemas.ClientCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    new_client = models.Client(
        client_name = client.client_name,
        created_by = str(current_user["user_id"])
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client

@router.get("/")
def get_client(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return db.query(models.Client).all()

@router.get("/{id}")
def get_client(id:int, db:Session=Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id==id).first()
    return client

@router.delete("/{id}",status_code=204)
def delete_client(id:int, db:Session=Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id==id).first()
    db.delete(client)
    db.commit()

