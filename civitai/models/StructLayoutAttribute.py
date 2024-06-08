from typing import *

from pydantic import BaseModel, Field

from .LayoutKind import LayoutKind


class StructLayoutAttribute(BaseModel):
    """
    None model

    """

    typeId: Optional[Any] = Field(alias="typeId", default=None)

    value: Optional[LayoutKind] = Field(alias="value", default=None)
