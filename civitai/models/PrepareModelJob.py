from typing import *

from pydantic import BaseModel, Field

from .BaseDiffusionModel import BaseDiffusionModel
from .PrepareModelAction import PrepareModelAction


class PrepareModelJob(BaseModel):
    """
    None model

    """

    baseModel: Optional[BaseDiffusionModel] = Field(alias="baseModel", default=None)

    model: Optional[str] = Field(alias="model", default=None)

    action: Optional[PrepareModelAction] = Field(alias="action", default=None)

    type: Optional[str] = Field(alias="type", default=None)
