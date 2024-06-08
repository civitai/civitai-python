from typing import *

from pydantic import BaseModel, Field


class ApplyConfigurationJob(BaseModel):
    """
    None model

    """

    configurationId: Optional[str] = Field(alias="configurationId", default=None)

    type: Optional[str] = Field(alias="type", default=None)
