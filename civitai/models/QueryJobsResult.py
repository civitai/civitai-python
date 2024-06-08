from typing import *

from pydantic import BaseModel, Field

from .JobStatus import JobStatus


class QueryJobsResult(BaseModel):
    """
    None model

    """

    cursor: Optional[str] = Field(alias="cursor", default=None)

    jobs: Optional[List[Optional[JobStatus]]] = Field(alias="jobs", default=None)
