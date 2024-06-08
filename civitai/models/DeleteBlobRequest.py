from typing import *

from pydantic import BaseModel, Field


class DeleteBlobRequest(BaseModel):
    """
    None model

    """

    key: Optional[str] = Field(alias="key", default=None)
