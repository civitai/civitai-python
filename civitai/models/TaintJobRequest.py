from typing import *

from pydantic import BaseModel, Field


class TaintJobRequest(BaseModel):
    """
    None model

    """

    reason: Optional[str] = Field(alias="reason", default=None)

    context: Optional[Dict[str, Any]] = Field(alias="context", default=None)
