from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.config import get_db
from app.schemas.Post import PostDto, Post
from app.service import PostService

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("")
async def get_all_posts(db: db_dependency):
    try:
        list_post = PostService.get_all(db)
        return list_post
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.post("", response_model=Post)
async def create_a_post(db: db_dependency, post: PostDto) -> Post:
    """
    :param db:
    :param post:
    :return:
    """
    try:
        created_post = PostService.add_post(db, post)
        return created_post
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.put("/{postId:str}", response_model=Post)
async def update_a_post(db: db_dependency, postId: str, post: PostDto) -> Post:
    try:
        updated_post = PostService.update_post(db, postId, post)
        return updated_post
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.delete("/{postId:str}")
async def update_a_post(postId: str, db: db_dependency):
    try:
        PostService.delete_post(db, postId)
        return {"meessage": "post is deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
