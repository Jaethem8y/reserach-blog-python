from typing import List, Union
from pydantic import BaseModel

class Content(BaseModel):
    order: int
    writing: Union[str, None] = None
    tag: Union[str, None] = None
    link: Union[str, None] = None
    image: Union[str, None] = None
    code: Union[str, None] = None
    important: Union[str, None] = None




    