from typing import List, Union
from pydantic import BaseModel

from src.DTO.Content import Content

class Post(BaseModel):
    title:str
    description: str
    category: str
    content: List[Content]


    