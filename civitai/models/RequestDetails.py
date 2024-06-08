from typing import *

from pydantic import BaseModel, Field

from .JobDetails import JobDetails


class RequestDetails(BaseModel):
    """
    None model

    """

    dateTime: Optional[str] = Field(alias="dateTime", default=None)

    jobs: Optional[List[Optional[JobDetails]]] = Field(alias="jobs", default=None)
