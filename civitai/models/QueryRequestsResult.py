from typing import *

from pydantic import BaseModel, Field

from .RequestDetails import RequestDetails
from .TelemetryCursor import TelemetryCursor


class QueryRequestsResult(BaseModel):
    """
    None model

    """

    cursor: Optional[TelemetryCursor] = Field(alias="cursor", default=None)

    requests: Optional[List[Optional[RequestDetails]]] = Field(alias="requests", default=None)
