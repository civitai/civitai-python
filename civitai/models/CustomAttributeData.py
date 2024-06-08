from typing import *

from pydantic import BaseModel, Field

class CustomAttributeData(BaseModel):
    """
    None model

    """

    attributeType: Optional["Type"] = Field(alias="attributeType", default=None)

    constructor: Optional["ConstructorInfo"] = Field(alias="constructor", default=None)

    constructorArguments: Optional[List[Optional["CustomAttributeTypedArgument"]]] = Field(
        alias="constructorArguments", default=None
    )

    namedArguments: Optional[List[Optional["CustomAttributeNamedArgument"]]] = Field(
        alias="namedArguments", default=None
    )

    class Config:
        arbitrary_types_allowed = True

from .ConstructorInfo import ConstructorInfo
from .CustomAttributeNamedArgument import CustomAttributeNamedArgument
from .CustomAttributeTypedArgument import CustomAttributeTypedArgument
from .Type import Type