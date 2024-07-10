from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.config import get_db
from app.schemas.Post import PostDto, Post
from app.service import post_service

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


# Configure logging


@router.get("")
async def get_all_posts(db: db_dependency) -> List[Post]:
    list_post = post_service.get_all(db)
    return list_post


@router.post("", response_model=Post)
async def create_a_post(db: db_dependency, post: PostDto) -> Post:
    """
    :param db:
    :param post:
    :return:
    """
    created_post = post_service.add_post(db, post)
    return created_post


@router.put("/{postId:str}", response_model=Post)
async def update_a_post(db: db_dependency, postId: str, post: PostDto) -> Post:
    updated_post = post_service.update_post(db, postId, post)
    return updated_post


@router.delete("/{postId:str}")
async def delete_a_post(postId: str, db: db_dependency):
    post_service.delete_post(db, postId)
