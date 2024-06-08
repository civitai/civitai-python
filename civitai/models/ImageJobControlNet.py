from typing import *

from pydantic import BaseModel, Field

from .ImageTransformer import ImageTransformer


class ImageJobControlNet(BaseModel):
    """
    None model

    """

    preprocessor: Optional[ImageTransformer] = Field(alias="preprocessor", default=None)

    weight: Optional[float] = Field(alias="weight", default=None)

    startStep: Optional[float] = Field(alias="startStep", default=None)

    endStep: Optional[float] = Field(alias="endStep", default=None)

    blobKey: Optional[str] = Field(alias="blobKey", default=None)

    imageUrl: Optional[str] = Field(alias="imageUrl", default=None)
