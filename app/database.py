from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your SQLAlchemy database URL for MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost/fastapi"

# Create the engine without the `connect_args` for MySQL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
