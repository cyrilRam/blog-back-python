import logging
from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.config import get_db
from app.schemas.Post import PostDto, Post
from app.service import post_service

router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("")
async def get_all_posts(db: db_dependency) -> List[Post]:
    try:
        logger.info("Fetching all posts")
        list_post = post_service.get_all(db)
        logger.info("Successfully fetched all posts")
        return list_post
    except Exception as e:
        logger.error(f"Error fetching all posts: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("", response_model=Post)
async def create_a_post(db: db_dependency, post: PostDto) -> Post:
    """
    :param db:
    :param post:
    :return:
    """
    try:
        logger.info(f"Creating a post with data: {post}")
        created_post = post_service.add_post(db, post)
        logger.info(f"Successfully created a post with ID: {created_post.id}")
        return created_post
    except Exception as e:
        logger.error(f"Error creating a post: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{postId:str}", response_model=Post)
async def update_a_post(db: db_dependency, postId: str, post: PostDto) -> Post:
    try:
        logger.info(f"Updating post with ID: {postId} with data: {post}")
        updated_post = post_service.update_post(db, postId, post)
        logger.info(f"Successfully updated post with ID: {updated_post.id}")
        return updated_post
    except Exception as e:
        logger.error(f"Error updating post with ID {postId}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{postId:str}")
async def delete_a_post(postId: str, db: db_dependency):
    try:
        logger.info(f"Deleting post with ID: {postId}")
        post_service.delete_post(db, postId)
        logger.info(f"Successfully deleted post with ID: {postId}")
        return {"message": "Post is deleted"}
    except Exception as e:
        logger.error(f"Error deleting post with ID {postId}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
