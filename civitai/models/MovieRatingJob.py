from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class MovieRatingJob(BaseModel):
    """
    None model

    """

    model: Optional[str] = Field(alias="model", default=None)

    mediaUrl: Optional[str] = Field(alias="mediaUrl", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    claimDuration: Optional[TimeSpan] = Field(alias="claimDuration", default=None)
