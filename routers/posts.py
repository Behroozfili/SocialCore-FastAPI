from fastapi import APIRouter,Depends
from db.database import get_db
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay
from db import db_user

router = APIRouter(prefix="/post", tags=["posts"])

@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)