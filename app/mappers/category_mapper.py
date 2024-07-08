from app.db.models import Category as modelCategory
from app.schemas.Category import Category


class CategoryMapper:
    
    @staticmethod
    def from_orm_to_schema(model: modelCategory) -> Category:
        category = Category(
            id=model.id,
            name=model.name,
        )
        return category
