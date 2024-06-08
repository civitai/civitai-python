from typing import *

from pydantic import BaseModel, Field

from .ImageJobControlNet import ImageJobControlNet
from .ImageJobParams import ImageJobParams
from .Priority import Priority
from .Provider import Provider
from .TimeSpan import TimeSpan


class TextToImageJobRequest(BaseModel):
    """
    None model

    """

    name: Optional[str] = Field(alias="name", default=None)

    priority: Optional[Priority] = Field(alias="priority", default=None)

    providers: Optional[List[Optional[Provider]]] = Field(alias="providers", default=None)

    expireAt: Optional[str] = Field(alias="expireAt", default=None)

    properties: Optional[Dict[str, Any]] = Field(alias="properties", default=None)

    callbackUrl: Optional[str] = Field(alias="callbackUrl", default=None)

    timeout: Optional[TimeSpan] = Field(alias="timeout", default=None)

    retries: Optional[int] = Field(alias="retries", default=None)

    dependencies: Optional[List[str]] = Field(alias="dependencies", default=None)

    quantity: Optional[int] = Field(alias="quantity", default=None)

    model: Optional[str] = Field(alias="model", default=None)

    additionalNetworks: Optional[Dict[str, Any]] = Field(alias="additionalNetworks", default=None)

    controlNets: Optional[List[Optional[ImageJobControlNet]]] = Field(alias="controlNets", default=None)

    params: Optional[ImageJobParams] = Field(alias="params", default=None)
