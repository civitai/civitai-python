from typing import *

from pydantic import BaseModel, Field


class ReadOnlySpan1(BaseModel):
    """
    None model

    """

    length: Optional[int] = Field(alias="length", default=None)

    isEmpty: Optional[bool] = Field(alias="isEmpty", default=None)
