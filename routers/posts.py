from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_post
from schemas import PostBase, PostDisplay


router = APIRouter(prefix="/post", tags=["posts"])
image_url_types = ["url", "upload"]

@router.post("/create_post", response_model=PostDisplay)
def create_user(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
         detail="image url type must be url or upload")
    return db_post.create_post(request, db)