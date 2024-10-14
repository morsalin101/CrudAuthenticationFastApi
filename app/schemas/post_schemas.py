from pydantic import BaseModel
from typing import Optional



class PostCreate(BaseModel):
    title: str
    description: str



class PostUpdate(BaseModel):
    title: str
    description: str    

