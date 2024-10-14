import uuid
from sqlalchemy.orm import Session
from app import models





def generate_uuid():
    return str(uuid.uuid4())


# Helper function to authenticate user
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(
         models.User.email == email, 
         models.User.password == password
         ).first()
    
    if not user:
        return False
    return user



