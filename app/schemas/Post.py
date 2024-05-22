from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4

from app.db.models import Post as ModelPost
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

    @classmethod
    def from_orm(cls, model: ModelPost) -> "Post":
        post = Post(
            id=model.id,
            title=model.title,
            content=model.content,
            created_date=model.created_date,
            category=Category.from_orm(model.category)
        )
        return post

    @classmethod
    def to_orm(cls, schema: "Post") -> "ModelPost":
        model_post = ModelPost(
            title=schema.title,
            content=schema.content,
            created_date=schema.created_date,
            category_id=schema.category.id  # Assuming Category has an id attribute
        )
        return model_post
