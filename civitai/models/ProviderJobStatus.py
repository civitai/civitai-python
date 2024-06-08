from typing import *

from pydantic import BaseModel, Field

from .JobSupport import JobSupport
from .ProviderJobQueuePosition import ProviderJobQueuePosition


class ProviderJobStatus(BaseModel):
    """
    None model

    """

    support: Optional[JobSupport] = Field(alias="support", default=None)

    queuePosition: Optional[ProviderJobQueuePosition] = Field(alias="queuePosition", default=None)
