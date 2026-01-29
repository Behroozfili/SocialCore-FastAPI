from db.models import User
from schemas import UserBase
from sqlalchemy.orm import Session
from db.hash import Hash
from fastapi import HTTPException,status


def create_user(request: UserBase,db:Session):
  user = User(
    username=request.username,
    email=request.email,
    password=Hash.bcrypt(request.password)
  )
  db.add(user)
  db.commit()
  db.refresh(user)
  return user

def get_user_by_username(db:Session,username:str):    
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user