from typing import *

from pydantic import BaseModel, Field

from .ImageTransformer import ImageTransformer


class ImageTransformJob(BaseModel):
    """
    None model

    """

    imageUrl: Optional[str] = Field(alias="imageUrl", default=None)

    transformer: Optional[ImageTransformer] = Field(alias="transformer", default=None)

    destinationBlobKey: Optional[str] = Field(alias="destinationBlobKey", default=None)

    params: Optional[Dict[str, Any]] = Field(alias="params", default=None)

    destinationUrl: Optional[str] = Field(alias="destinationUrl", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    type: Optional[str] = Field(alias="type", default=None)
