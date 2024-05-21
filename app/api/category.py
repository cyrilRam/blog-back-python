from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.config import get_db
from app.schemas.Post import Post

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


# @router.get("/all_posts")
# async def get_all_posts(db: db_dependency):
#     try:
#         list_post = Post.get_all(db)
#         return list_post
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=e)
#
#
# @router.post("create_post")
# async def create_a_post(db: db_dependency, post: Post):
#     try:
#         Post.add_post(db, post)
#         return {"message": "Post créé avec succès"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=e)
