from pydantic import UUID4

from app.db.models import Category as ModelCategory
from app.schemas.Category import Category, CategoryNotFoundException


def category_by_id(db, category_id: UUID4) -> Category:
    # Implémentez la logique pour récupérer la catégorie à partir de son ID dans la base de données
    # Supposons que vous ayez une méthode dans votre modèle SQLAlchemy pour récupérer une catégorie par son ID
    # Remplacez la ligne suivante par la logique réelle
    category_orm = db.query(ModelCategory).filter(ModelCategory.id == category_id).first()
    if not category_orm:
        raise CategoryNotFoundException(f"No category found with ID {category_id}")
    return Category(id=category_orm.id, name=category_orm.name)


def get_all(db) -> [Category]:
    list_models = db.query(ModelCategory).all()
    list_schemas = [Category.from_orm(category) for category in list_models]
    return list_schemas
