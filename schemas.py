from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str
    department: str
    position: str


class UserLogin(BaseModel):
    username: str
    password: str
