from typing import *

from pydantic import BaseModel, Field

from .CustomAttributeData import CustomAttributeData
from .MemberInfo import MemberInfo
from .ParameterAttributes import ParameterAttributes
from .Type import Type


class ParameterInfo(BaseModel):
    """
    None model

    """

    attributes: Optional[ParameterAttributes] = Field(alias="attributes", default=None)

    member: Optional[MemberInfo] = Field(alias="member", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    parameterType: Optional[Type] = Field(alias="parameterType", default=None)

    position: Optional[int] = Field(alias="position", default=None)

    isIn: Optional[bool] = Field(alias="isIn", default=None)

    isLcid: Optional[bool] = Field(alias="isLcid", default=None)

    isOptional: Optional[bool] = Field(alias="isOptional", default=None)

    isOut: Optional[bool] = Field(alias="isOut", default=None)

    isRetval: Optional[bool] = Field(alias="isRetval", default=None)

    defaultValue: Optional[Any] = Field(alias="defaultValue", default=None)

    rawDefaultValue: Optional[Any] = Field(alias="rawDefaultValue", default=None)

    hasDefaultValue: Optional[bool] = Field(alias="hasDefaultValue", default=None)

    customAttributes: Optional[List[Optional[CustomAttributeData]]] = Field(alias="customAttributes", default=None)

    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)
