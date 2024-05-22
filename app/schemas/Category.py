from typing import Optional, Union

from pydantic import BaseModel, UUID4

from app.db.models import Category as modelCategory


class CategoryNotFoundException(Exception):
    pass


class Category(BaseModel):
    id: Optional[Union[UUID4, None]]
    name: str

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, model: modelCategory) -> "Category":
        category = Category(
            id=model.id,
            name=model.name,
        )
        return category
