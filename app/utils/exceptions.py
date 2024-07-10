import logging
from typing import Type

from fastapi import HTTPException

from app.utils.logger import logger


class CustomException(HTTPException):
    def __init__(self, status_code: int, detail: str, log_level: int):
        super().__init__(status_code=status_code, detail=detail)
        self.log_level = log_level
        logger.log(self.log_level, f"Custom error {type(self).__name__} occurred: {self.detail}")


class ObjectNotFound(CustomException):
    def __init__(self, object_type: Type, id_object: str):
        detail = f"The {object_type.__name__} with id {id_object} doesn't exist"
        super().__init__(status_code=404, detail=detail, log_level=logging.ERROR)


class ErrorConnectionDB(CustomException):
    def __init__(self, message):
        detail = f"The connection to the db has failed. {message} "
        super().__init__(status_code=503, detail=detail, log_level=logging.ERROR)
