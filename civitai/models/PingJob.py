from typing import *

from pydantic import BaseModel, Field


class PingJob(BaseModel):
    """
    None model

    """

    type: Optional[str] = Field(alias="type", default=None)
