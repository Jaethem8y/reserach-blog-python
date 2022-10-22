from typing import List, Union
from pydantic import BaseModel

class Login(BaseModel):
    username: str
    password: str
   