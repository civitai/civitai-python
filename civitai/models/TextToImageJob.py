from typing import *

from pydantic import BaseModel, Field

from .BaseDiffusionModel import BaseDiffusionModel
from .ImageJobControlNet import ImageJobControlNet
from .ImageJobParams import ImageJobParams
from .TimeSpan import TimeSpan


class TextToImageJob(BaseModel):
    """
    None model

    """

    model: Optional[str] = Field(alias="model", default=None)

    params: Optional[ImageJobParams] = Field(alias="params", default=None)

    imageHash: Optional[str] = Field(alias="imageHash", default=None)

    additionalNetworks: Optional[Dict[str, Any]] = Field(alias="additionalNetworks", default=None)

    destinationUrl: Optional[str] = Field(alias="destinationUrl", default=None)

    baseModel: Optional[BaseDiffusionModel] = Field(alias="baseModel", default=None)

    storeAsBlob: Optional[bool] = Field(alias="storeAsBlob", default=None)

    controlNets: Optional[List[Optional[ImageJobControlNet]]] = Field(alias="controlNets", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    claimDuration: Optional[TimeSpan] = Field(alias="claimDuration", default=None)

    type: Optional[str] = Field(alias="type", default=None)
