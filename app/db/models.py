from sqlalchemy import Column, ForeignKey, String, Text, TIMESTAMP
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    name = Column(String(100), unique=True)

    posts = relationship("Post", back_populates="category")  # Define reverse relationship


class Post(Base):
    __tablename__ = 'post'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())
    title = Column(String(100))
    content = Column(Text)
    created_date = Column(TIMESTAMP)
    category_id = Column(String, ForeignKey('category.id'))

    category = relationship("Category", back_populates="posts")
