from typing import *

from pydantic import BaseModel, Field


class ProblemDetails(BaseModel):
    """
    None model

    """

    type: Optional[str] = Field(alias="type", default=None)

    title: Optional[str] = Field(alias="title", default=None)

    status: Optional[int] = Field(alias="status", default=None)

    detail: Optional[str] = Field(alias="detail", default=None)

    instance: Optional[str] = Field(alias="instance", default=None)
