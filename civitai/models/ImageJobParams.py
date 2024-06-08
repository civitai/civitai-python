from typing import *

from pydantic import BaseModel, Field

from .Scheduler import Scheduler


class ImageJobParams(BaseModel):
    """
    None model

    """

    prompt: Optional[str] = Field(alias="prompt", default=None)

    negativePrompt: Optional[str] = Field(alias="negativePrompt", default=None)

    scheduler: Optional[Scheduler] = Field(alias="scheduler", default=None)

    steps: Optional[int] = Field(alias="steps", default=None)

    cfgScale: Optional[float] = Field(alias="cfgScale", default=None)

    width: int = Field(alias="width")

    height: int = Field(alias="height")

    seed: Optional[int] = Field(alias="seed", default=None)

    clipSkip: Optional[int] = Field(alias="clipSkip", default=None)
