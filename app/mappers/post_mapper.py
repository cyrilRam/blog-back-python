from app.db.models import Post as ModelPost
from app.mappers.category_mapper import CategoryMapper

from app.schemas.Post import Post


class PostMapper:
    @staticmethod
    def from_orm_to_schema(model: ModelPost) -> "Post":
        post = Post(
            id=model.id,
            title=model.title,
            content=model.content,
            created_date=model.created_date,
            category=CategoryMapper.from_orm_to_schema(model.category)
        )
        return post
