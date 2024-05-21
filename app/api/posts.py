from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.db.config import get_db
from app.schemas.Post import Post, PostDto

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("")
#TODO:faire par date de creation
async def get_all_posts(db: db_dependency):
    try:
        list_post = Post.get_all(db)
        return list_post
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.post("")
#TODO:ajouter le return du post
async def create_a_post(db: db_dependency, post: PostDto):
    """
    ajouter le return du post
    :param db:
    :param post:
    :return:
    """
    try:
        Post.add_post(db, post)
        return {"message": "Post créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


@router.put("/{postId:str}")
async def get_all_posts(db: db_dependency,postId:str,post:PostDto):
    try:
        # list_post = Post.get_all(db)
        # return list_post
        return {"message": "Post créé avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)