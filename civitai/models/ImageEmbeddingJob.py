from typing import *

from pydantic import BaseModel, Field


class ImageEmbeddingJob(BaseModel):
    """
    None model

    """

    imageUrl: Optional[str] = Field(alias="imageUrl", default=None)

    type: Optional[str] = Field(alias="type", default=None)
