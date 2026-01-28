from db.models import User,Post
from schemas import PostBase
from sqlalchemy.orm import Session


def create_post(request: PostBase, db: Session):
    
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
