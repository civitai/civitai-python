from typing import *

from pydantic import BaseModel, Field


class ModuleHandle(BaseModel):
    """
    None model

    """

    mdStreamVersion: Optional[int] = Field(alias="mdStreamVersion", default=None)
