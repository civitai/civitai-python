from typing import *

from pydantic import BaseModel, Field


class TaintJobsResult(BaseModel):
    """
    None model

    """

    jobs: Optional[int] = Field(alias="jobs", default=None)
