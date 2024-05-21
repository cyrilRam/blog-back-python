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

    @classmethod
    def category_by_id(cls, db, category_id: UUID4) -> "Category":
        # Implémentez la logique pour récupérer la catégorie à partir de son ID dans la base de données
        # Supposons que vous ayez une méthode dans votre modèle SQLAlchemy pour récupérer une catégorie par son ID
        # Remplacez la ligne suivante par la logique réelle
        category_orm = db.query(modelCategory).filter(modelCategory.id == category_id).first()
        if not category_orm:
            raise CategoryNotFoundException(f"No category found with ID {category_id}")
        return Category(id=category_orm.id, name=category_orm.name)
