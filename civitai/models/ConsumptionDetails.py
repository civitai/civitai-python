from typing import *

from pydantic import BaseModel, Field


class ConsumptionDetails(BaseModel):
    """
    None model

    """

    images: Optional[int] = Field(alias="images", default=None)

    totalCost: Optional[float] = Field(alias="totalCost", default=None)

    startDate: Optional[str] = Field(alias="startDate", default=None)

    endDate: Optional[str] = Field(alias="endDate", default=None)
