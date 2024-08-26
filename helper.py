import uuid
from passlib.context import CryptContext
from sqlalchemy.orm import Session
import models
from fastapi import Depends, HTTPException, status
from database import get_db
import jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta,timezone
import schemas.user_schemas 



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



