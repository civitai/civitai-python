from typing import *

from pydantic import BaseModel, Field

from .AssetType import AssetType


class ImageJobNetworkParams(BaseModel):
    """
    None model

    """

    type: Optional[AssetType] = Field(alias="type", default=None)

    strength: Optional[float] = Field(alias="strength", default=None)

    triggerWord: Optional[str] = Field(alias="triggerWord", default=None)
