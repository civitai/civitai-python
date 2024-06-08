from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class ComfyJob(BaseModel):
    """
    None model

    """

    params: Optional[Any] = Field(alias="params", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    claimDuration: Optional[TimeSpan] = Field(alias="claimDuration", default=None)
