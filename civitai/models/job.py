from typing import *

from pydantic import BaseModel, Field

from .TimeSpan import TimeSpan


class Job(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    createdAt: Optional[str] = Field(alias="createdAt", default=None)

    expireAt: Optional[str] = Field(alias="expireAt", default=None)

    webhook: Optional[str] = Field(alias="webhook", default=None)

    properties: Optional[Dict[str, Any]] = Field(alias="properties", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    cost: Optional[float] = Field(alias="cost", default=None)

    maxRetryAttempt: Optional[int] = Field(alias="maxRetryAttempt", default=None)

    dependencies: Optional[List[str]] = Field(alias="dependencies", default=None)

    issuedBy: Optional[str] = Field(alias="issuedBy", default=None)

    claimDuration: Optional[TimeSpan] = Field(alias="claimDuration", default=None)
