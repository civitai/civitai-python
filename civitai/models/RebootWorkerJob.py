from typing import *

from pydantic import BaseModel, Field


class RebootWorkerJob(BaseModel):
    """
    None model

    """

    type: Optional[str] = Field(alias="type", default=None)
