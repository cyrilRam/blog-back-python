from datetime import datetime
from typing import Any

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models import Post as ModelPost
from app.schemas.Post import Post, PostDto


def get_all(db) -> [Post]:
    list_models = db.query(ModelPost).order_by(ModelPost.created_date.desc()).all()
    list_schemas = [Post.from_orm(post) for post in list_models]
    return list_schemas


def add_post(db: Session, post_to_add: PostDto) -> Post:
    try:
        model_post = ModelPost(title=post_to_add.title, content=post_to_add.content, category_id=post_to_add.categoryId,
                               created_date=datetime.now())
        db.add(model_post)
        db.commit()
        db.refresh(model_post)
        post = Post.from_orm(model_post)
        return post
    except Exception as e:
        db.rollback()
        raise e


def update_post(db: Session, post_id: str, post_data: PostDto) -> Post:
    try:
        post_model: Any = db.query(ModelPost).filter(ModelPost.id == post_id).first()
        if not post_model:
            raise HTTPException(status_code=404, detail="Post non trouvé")

        post_model.title = post_data.title
        post_model.content = post_data.content
        post_model.category_id = post_data.categoryId

        db.commit()
        db.refresh(post_model)
        post = Post.from_orm(post_model)
        return post
    except Exception as e:
        db.rollback()
        raise e


def delete_post(db: Session, post_id: str):
    try:
        post = db.query(ModelPost).filter(ModelPost.id == post_id).first()
        if not post:
            raise HTTPException(status_code=404, detail="Post non trouvé")
        db.delete(post)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
