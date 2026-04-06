from fastapi import FastAPI
from .database import engine
from .import models
from app.routers import users,auth
from app.routers import clients

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(clients.router)

@app.get("/")
def home():
    return {"message": "API is working"}
