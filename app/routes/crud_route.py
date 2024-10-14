from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from models import Post, User
from database import get_db
from schemas.post_schemas import PostCreate, PostUpdate  # Assuming PostUpdate is defined
from auth import get_current_user

# Define the HTTPBearer dependency
security = HTTPBearer()

router = APIRouter()

@router.get("/all-posts")
def get_posts(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Use the credentials.token if needed
    posts = db.query(Post).all()
    return posts

@router.post("/posts/", response_model=PostCreate)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security),
    current_user: User = Depends(get_current_user)
):
    # credentials.token gives you the token from the Authorization header
    db_post = Post(title=post.title, description=post.description, uuid=post.uuid)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/post/{post_id}")
def get_post_by_id(post_id: int, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/update-post/{post_id}")
def update_post(
    post_id: int,
    post: PostUpdate,
    db: Session = Depends(get_db),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db_post.title = post.title
    db_post.description = post.description
    db.commit()
    db.refresh(db_post)  # Refresh to return the updated object
    return {"message": "Post updated successfully", "post": db_post}

@router.delete("/delete-post/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Depends(security)):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(db_post)
    db.commit()
    return {"message": "Post deleted successfully"}
