from typing import *

from pydantic import BaseModel, Field


class QueryJobsRequest(BaseModel):
    """
    None model

    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    jobType: Optional[str] = Field(alias="jobType", default=None)

    properties: Optional[Dict[str, Any]] = Field(alias="properties", default=None)
