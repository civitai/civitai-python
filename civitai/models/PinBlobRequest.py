from typing import *

from pydantic import BaseModel, Field


class PinBlobRequest(BaseModel):
    """
    None model

    """

    key: Optional[str] = Field(alias="key", default=None)
