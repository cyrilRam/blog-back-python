from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4

from app.schemas.Category import Category


class PostDto(BaseModel):
    title: str
    content: str
    categoryId: UUID4


class Post(BaseModel):
    id: UUID4
    title: str
    content: str
    created_date: Optional[datetime]
    category: Category

    class Config:
        orm_mode = True
