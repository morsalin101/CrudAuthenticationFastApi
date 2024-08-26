from fastapi import APIRouter

router = APIRouter()





@router.post("/signup")
def create_user():
    return {"message": "User created"}


@router.post("/login")
def login():
    return {"message": "login"}


@router.post("/logout")
def logout():
    return {"message": "logout"}