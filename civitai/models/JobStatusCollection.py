from typing import *

from pydantic import BaseModel, Field

from .JobStatus import JobStatus


class JobStatusCollection(BaseModel):
    """
    None model

    """

    token: Optional[str] = Field(alias="token", default=None)

    jobs: Optional[List[Optional[JobStatus]]] = Field(alias="jobs", default=None)
