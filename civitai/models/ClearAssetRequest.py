from typing import *

from pydantic import BaseModel, Field


class ClearAssetRequest(BaseModel):
    """
    None model

    """

    jobId: Optional[str] = Field(alias="jobId", default=None)
