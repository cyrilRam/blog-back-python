from datetime import datetime
from typing import Optional, Union

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

    @staticmethod
    def get_all(db):
        list_models = db.query(ModelPost).all()
        list_schemas = [Post.from_orm(post) for post in list_models]
        return list_schemas

    @staticmethod
    def add_post(db, post_to_add:PostDto):
        try:
            model=ModelPost(title=post_to_add.title,content=post_to_add.content,category_id=post_to_add.categoryId,created_date=datetime.now())
            db.add(model)
            db.commit()
            db.refresh(model)
        except Exception as e:
            db.rollback()
            raise e
