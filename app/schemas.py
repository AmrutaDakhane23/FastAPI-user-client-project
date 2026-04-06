from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : int
    name : str
    email : str

    class Config:
        from_attributes = True

class ClientCreate(BaseModel):
    client_name : str

class ClientOut(BaseModel):
    id : int
    client_name:str
    created_by :str

    class Config:
        from_attributes = True

