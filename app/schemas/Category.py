from typing import Optional, Union

from pydantic import BaseModel, UUID4


class CategoryNotFoundException(Exception):
    pass


class Category(BaseModel):
    id: Optional[Union[UUID4, None]]
    name: str

    class Config:
        orm_mode = True
