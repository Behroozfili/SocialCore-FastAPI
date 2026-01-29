from db.models import User,Post
from schemas import PostBase
from sqlalchemy.orm import Session
from fastapi import HTTPException,status



def create_post(db: Session, request: PostBase):
    
    new_post = Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=request.timestamp,
        user_id=request.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    posts = db.query(Post).all()
    return posts

def delete_post(db: Session, id: int,user_id:int):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="You are not authorized to delete this post")
    db.delete(post)
    db.commit()
    return {"message":"Post deleted successfully"}