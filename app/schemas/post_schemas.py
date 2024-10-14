from pydantic import BaseModel
from typing import Optional



class PostCreate(BaseModel):
    title: str
    description: str
    uuid:Optional[str] = None 


class PostUpdate(BaseModel):
    title: str
    description: str    

