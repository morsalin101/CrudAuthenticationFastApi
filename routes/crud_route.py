from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models import Post
from database import SessionLocal
from schemas.post_schemas import PostCreate

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()


@router.get("/all-posts")
def get_post():
    return {"message": "List of users"}

@router.post("/posts/", response_model=PostCreate)
def create_post(post: PostCreate,db: Session = Depends(get_db)):
    db_post = Post(title=post.title, description=post.description, uuid=post.uuid)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.put("/update-post/{post_id}")
def update_post():
    return {"message": "User post"}

@router.delete("/delete-post/{post_id}")
def delete_post():
    return {"message": "User deleted"}
