from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class GetBlobRequest(BaseModel):
    """
    None model

    """

    key: Optional[str] = Field(alias="key", default=None)

    duration: Optional[TimeSpan] = Field(alias="duration", default=None)
