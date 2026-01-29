from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status
from typing import Optional
from datetime import datetime,timedelta
from jose import JWTError, jwt
from fastapi import Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db.db_user import get_user_by_username


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# openssl rand -hex 32
secret_key = "29bb0ffe6b135e99697e9d1906c9a6fd49e7e89586a9c12326ead1c7998b8a12"
algorithm = "HS256"
access_token_expire_minutes = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db,username)
    if user is None:
        raise credentials_exception
    return user