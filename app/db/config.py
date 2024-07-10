import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.utils.exceptions import ErrorConnectionDB

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSEWORD = os.getenv("DB_PASSEWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

URL_DB = f"postgresql://{DB_USER}:{DB_PASSEWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(URL_DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except OperationalError as e:
        raise ErrorConnectionDB(str(e))
    finally:
        db.close()
