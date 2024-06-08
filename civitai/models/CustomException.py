from typing import *

from pydantic import BaseModel, Field

from .MethodBase import MethodBase


class CustomException(BaseModel):
    """
    None model
    """

    targetSite: Optional[MethodBase] = Field(alias="targetSite", default=None)
    message: Optional[str] = Field(alias="message", default=None)
    data: Optional[Dict[str, Any]] = Field(alias="data", default=None)
    innerException: Optional["CustomException"] = Field(alias="innerException", default=None)
    helpLink: Optional[str] = Field(alias="helpLink", default=None)
    source: Optional[str] = Field(alias="source", default=None)
    hResult: Optional[int] = Field(alias="hResult", default=None)
    stackTrace: Optional[str] = Field(alias="stackTrace", default=None)
