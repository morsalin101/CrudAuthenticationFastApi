# app/main.py

from fastapi import FastAPI
from app.routes import crud_route, user_route  # Correct import path
from app.database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routers
app.include_router(crud_route.router,tags=["crud"])
app.include_router(user_route.router,tags=["user"])
