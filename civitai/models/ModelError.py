from typing import *

from pydantic import BaseModel, Field

from .CustomException import CustomException


class ModelError(BaseModel):
    """
    None model
    """

    exception: Optional[CustomException] = Field(alias="exception", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    stackTrace: Optional[str] = Field(alias="stackTrace", default=None)
