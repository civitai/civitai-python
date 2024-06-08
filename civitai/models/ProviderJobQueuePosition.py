from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class ProviderJobQueuePosition(BaseModel):
    """
    None model

    """

    precedingJobs: Optional[int] = Field(alias="precedingJobs", default=None)

    precedingCost: Optional[float] = Field(alias="precedingCost", default=None)

    throughputRate: Optional[float] = Field(alias="throughputRate", default=None)

    workerId: Optional[str] = Field(alias="workerId", default=None)

    estimatedStartDuration: Optional[TimeSpan] = Field(alias="estimatedStartDuration", default=None)

    estimatedStartDate: Optional[str] = Field(alias="estimatedStartDate", default=None)
