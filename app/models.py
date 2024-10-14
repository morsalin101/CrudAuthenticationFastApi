from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    uuid = Column(String(36), unique=True, index=True)  # Ensure this is unique and indexed

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True)
    description = Column(String(1000), index=True)
    uuid = Column(String(36), ForeignKey('users.uuid'))  # The uuid field references the user's UUID

    user = relationship("User", back_populates="posts")
