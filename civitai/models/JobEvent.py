from typing import *

from pydantic import BaseModel, Field

from .JobEventType import JobEventType
from .Provider import Provider


class JobEvent(BaseModel):
    """
    None model

    """

    jobId: Optional[str] = Field(alias="jobId", default=None)
    type: Optional[JobEventType] = Field(alias="type", default=None)
    dateTime: Optional[str] = Field(alias="dateTime", default=None)
    provider: Optional[Provider] = Field(alias="provider", default=None)
    workerId: Optional[str] = Field(alias="workerId", default=None)
    context: Optional[Dict[str, Any]] = Field(alias="context", default=None)
    claimDuration: Optional[str] = Field(alias="claimDuration", default=None)  
    jobDuration: Optional[str] = Field(alias="jobDuration", default=None)
    retryAttempt: Optional[int] = Field(alias="retryAttempt", default=None)
    cost: Optional[float] = Field(alias="cost", default=None)
    jobProperties: Optional[Dict[str, Any]] = Field(alias="jobProperties", default=None)
    jobType: Optional[str] = Field(alias="jobType", default=None)
    jobPriority: Optional[int] = Field(alias="jobPriority", default=None)
    claimHasCompleted: Optional[bool] = Field(alias="claimHasCompleted", default=None)
    jobHasCompleted: Optional[bool] = Field(alias="jobHasCompleted", default=None)