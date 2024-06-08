from typing import *

from pydantic import BaseModel, Field

from .Type import Type


class CustomAttributeTypedArgument(BaseModel):
    """
    None model

    """

    argumentType: Optional[Type] = Field(alias="argumentType", default=None)

    value: Optional[Any] = Field(alias="value", default=None)
