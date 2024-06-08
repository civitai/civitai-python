from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class WDTaggingJob(BaseModel):
    """
    None model

    """

    model: Optional[str] = Field(alias="model", default=None)

    mediaUrl: Optional[str] = Field(alias="mediaUrl", default=None)

    threshold: Optional[float] = Field(alias="threshold", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    claimDuration: Optional[TimeSpan] = Field(alias="claimDuration", default=None)

    type: Optional[str] = Field(alias="type", default=None)
