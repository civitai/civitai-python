from typing import *

from pydantic import BaseModel, Field

from .BaseDiffusionModel import BaseDiffusionModel
from .ReadOnlySpan1 import ReadOnlySpan1


class AIR(BaseModel):
    """
    None model

    """

    value: Optional[str] = Field(alias="value", default=None)

    legacyId: Optional[str] = Field(alias="legacyId", default=None)

    baseModel: Optional[BaseDiffusionModel] = Field(alias="baseModel", default=None)

    ecosystem: Optional[ReadOnlySpan1] = Field(alias="ecosystem", default=None)

    type: Optional[ReadOnlySpan1] = Field(alias="type", default=None)

    source: Optional[ReadOnlySpan1] = Field(alias="source", default=None)

    id: Optional[ReadOnlySpan1] = Field(alias="id", default=None)

    layer: Optional[ReadOnlySpan1] = Field(alias="layer", default=None)

    format: Optional[ReadOnlySpan1] = Field(alias="format", default=None)
