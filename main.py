from fastapi import FastAPI
from routes import user_route,crud_route  # Import your routers
from database import engine, Base
from sqlalchemy.orm import Session
import models

Base.metadata.create_all(bind=engine)


app = FastAPI()

# Include your routers
app.include_router(user_route.router,tags=["Users"])
app.include_router(crud_route.router,tags=["Crud"])


