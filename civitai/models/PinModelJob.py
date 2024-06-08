from typing import *

from pydantic import BaseModel, Field


class PinModelJob(BaseModel):
    """
    None model

    """

    assets: Optional[Dict[str, Any]] = Field(alias="assets", default=None)

    type: Optional[str] = Field(alias="type", default=None)
