import os
import random
import string
import shutil
from typing import List
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_post
from schemas import PostBase, PostDisplay,UserAuth
from auth.oath2 import get_current_user
from db import models


router = APIRouter(prefix="/post", tags=["posts"])

image_url_types = ["url", "upload"]


@router.post("/create_post", response_model=PostDisplay)
def create_post(request: PostBase,
 db: Session = Depends(get_db),
 current_user:UserAuth=Depends(get_current_user)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="image_url_type must be 'url' or 'upload'"
        )

    return db_post.create_post(db, request)


@router.get("/all", response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


@router.post("/upload_file")
def upload_file(file: UploadFile = File(...)):
    if not os.path.exists("images"):
        os.makedirs("images")
    
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    _, extension = os.path.splitext(file.filename)
    filename = f"{rand_str}{extension}"
    
    path_file = os.path.join("images", filename) 
    with open(path_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    
    return {"filename": filename,
            "path_file": path_file}

@router.delete("/delete_post/{id}")
def delete_post(id:int,db:Session=Depends(get_db),current_user:UserAuth=Depends(get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    db.delete(post)
    db.commit()
    return {"message":"Post deleted successfully"}