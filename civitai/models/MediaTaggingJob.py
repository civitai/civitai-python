from typing import *

from pydantic import BaseModel, Field


class MediaTaggingJob(BaseModel):
    """
    None model

    """

    modelId: Optional[int] = Field(alias="modelId", default=None)

    mediaUrl: Optional[str] = Field(alias="mediaUrl", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    type: Optional[str] = Field(alias="type", default=None)
