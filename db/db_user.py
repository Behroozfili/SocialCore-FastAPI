from db.models import User
from schemas import UserBase
from sqlalchemy.orm import Session


def create_user(request: UserBase,db:Session):
  user = User(
    username=request.username,
    email=request.email,
    password=request.password)
  db.add(user)
  db.commit()
  db.refresh(user)
  return user
    