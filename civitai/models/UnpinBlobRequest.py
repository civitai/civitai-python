from typing import *

from pydantic import BaseModel, Field


class UnpinBlobRequest(BaseModel):
    """
    None model

    """

    key: Optional[str] = Field(alias="key", default=None)
