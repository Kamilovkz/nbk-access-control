from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserLogin
from utils import hash_password, verify_password, create_access_token
from datetime import timedelta

app = FastAPI()


@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        hashed_password=hashed_password,
        department=user.department,
        position=user.position,
    )
    db.add(new_user)
    db.commit()
    return {"msg": "User registered seccessfully"}


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db.user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token_expires = timedelta(minutes=10)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
