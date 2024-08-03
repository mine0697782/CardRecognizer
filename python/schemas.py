from typing import List, Union
from pydantic import BaseModel

class CardBase(BaseModel):
    title: str
    description: Union[str, None] = None

# class CardCreate(ItemBase):
    # pass

