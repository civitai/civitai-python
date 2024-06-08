from typing import *

from pydantic import BaseModel, Field

from .IntPtr import IntPtr


class RuntimeTypeHandle(BaseModel):
    """
    None model

    """

    value: Optional[IntPtr] = Field(alias="value", default=None)
