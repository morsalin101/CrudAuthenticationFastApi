from fastapi import FastAPI
from routes import userRoute  # Import your routers

app = FastAPI()

# Include your routers
app.include_router(userRoute.router)


