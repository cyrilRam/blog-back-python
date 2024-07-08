from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.config import get_db
from app.service import category_service

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]


@router.get("")
async def get_all(db: db_dependency):
    try:
        list_category = category_service.get_all(db)
        return list_category
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
#
#
# @router.post("create_post")
# async def create_a_post(db: db_dependency, post: Post):
#     try:
#         Post.add_post(db, post)
#         return {"message": "Post créé avec succès"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=e)
