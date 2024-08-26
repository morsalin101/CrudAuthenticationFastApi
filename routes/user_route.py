from fastapi import APIRouter,Depends,status
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException
import schemas.user_schemas 
import models
import helper  
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token
from helper import authenticate_user

router = APIRouter(
    prefix="/auth"
)





@router.post("/signup")
def create_user(db: Session = Depends(get_db),user: schemas.user_schemas .UserCreate = Depends()):
    existing_user = db.query(models.User).filter_by(email=user.email).first()
    if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

    uuid = helper.generate_uuid()
    new_user = models.User(username=user.username,email=user.email, password=user.password,uuid=uuid) 
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"user created successfully"}


@router.post("/login", response_model=schemas.user_schemas.Token)
def login_for_access_token(form_data:schemas.user_schemas.UserLogin , db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(subject=user.username)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
def logout():
    return {"message": "logout"}