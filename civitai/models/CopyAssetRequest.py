from typing import *

from pydantic import BaseModel, Field


class CopyAssetRequest(BaseModel):
    """
    None model

    """

    jobId: Optional[str] = Field(alias="jobId", default=None)

    assetName: Optional[str] = Field(alias="assetName", default=None)

    destinationUri: Optional[str] = Field(alias="destinationUri", default=None)
