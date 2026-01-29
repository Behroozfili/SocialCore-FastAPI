from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from db.database import get_db
from db import models
from sqlalchemy.orm import Session
from db.hash import Hash
from auth.oath2 import create_access_token
 


router = APIRouter( tags=["authentication"])

@router.post("/token")
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")
    access_token = create_access_token(data={"sub":user.username})
    return {"access_token":access_token,
    "token_type":"bearer",
    "user_id":user.id,
    "username":user.username}