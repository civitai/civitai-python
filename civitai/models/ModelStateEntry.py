from typing import *

from pydantic import BaseModel, Field

from .ModelError import ModelError
from .ModelValidationState import ModelValidationState


class ModelStateEntry(BaseModel):
    """
    None model

    """

    rawValue: Optional[Any] = Field(alias="rawValue", default=None)

    attemptedValue: Optional[str] = Field(alias="attemptedValue", default=None)

    errors: Optional[List[Optional[ModelError]]] = Field(alias="errors", default=None)

    validationState: Optional[ModelValidationState] = Field(alias="validationState", default=None)

    isContainerNode: Optional[bool] = Field(alias="isContainerNode", default=None)

    children: Optional[List[Optional["ModelStateEntry"]]] = Field(alias="children", default=None)
