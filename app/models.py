from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))  # Specify length
    email = Column(String(255), unique=True, index=True)  # Specify length
    password = Column(String(255))  # Specify length
    uuid = Column(String(36))  # Typically UUIDs have a fixed length of 36 characters
    

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True)  # Specify length
    description = Column(String(1000), index=True)  # Specify length based on your expected text size
    uuid = Column(String(36))  # Specify length (UUID is 36 characters)
