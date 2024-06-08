from typing import *

from pydantic import BaseModel, Field

from .WorkerAssetAvailability import WorkerAssetAvailability


class ProviderAssetAvailability(BaseModel):
    """
    None model

    """

    availability: Optional[WorkerAssetAvailability] = Field(alias="availability", default=None)

    workers: Optional[int] = Field(alias="workers", default=None)
