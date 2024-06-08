from typing import *

from pydantic import BaseModel, Field


class TelemetryCursor(BaseModel):
    """
    None model

    """

    nextDateTime: Optional[str] = Field(alias="nextDateTime", default=None)

    nextId: Optional[str] = Field(alias="nextId", default=None)
