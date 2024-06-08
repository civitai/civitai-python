from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class ImageResourceTrainingJob(BaseModel):
    """
    None model

    """

    model: Optional[str] = Field(alias="model", default=None)

    trainingData: Optional[str] = Field(alias="trainingData", default=None)

    params: Optional[Dict[str, Any]] = Field(alias="params", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    customCost: Optional[float] = Field(alias="customCost", default=None)

    output: Optional[str] = Field(alias="output", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    claimDuration: Optional[TimeSpan] = Field(alias="claimDuration", default=None)
