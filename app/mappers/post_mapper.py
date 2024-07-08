from app.db.models import Post as ModelPost
from app.schemas.Category import Category
from app.schemas.Post import Post


class PostMapper:
    @staticmethod
    def from_orm_to_schema(model: ModelPost) -> "Post":
        post = Post(
            id=model.id,
            title=model.title,
            content=model.content,
            created_date=model.created_date,
            category=Category.from_orm(model.category)
        )
        return post