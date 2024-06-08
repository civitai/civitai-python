from typing import *

from pydantic import BaseModel, Field

from .CustomAttributeData import CustomAttributeData
from .MemberTypes import MemberTypes
from .MethodInfo import MethodInfo
from .Module import Module
from .PropertyAttributes import PropertyAttributes
from .Type import Type


class PropertyInfo(BaseModel):
    """
    None model

    """

    name: Optional[str] = Field(alias="name", default=None)

    declaringType: Optional[Type] = Field(alias="declaringType", default=None)

    reflectedType: Optional[Type] = Field(alias="reflectedType", default=None)

    module: Optional[Module] = Field(alias="module", default=None)

    customAttributes: Optional[List[Optional[CustomAttributeData]]] = Field(alias="customAttributes", default=None)

    isCollectible: Optional[bool] = Field(alias="isCollectible", default=None)

    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)

    memberType: Optional[MemberTypes] = Field(alias="memberType", default=None)

    propertyType: Optional[Type] = Field(alias="propertyType", default=None)

    attributes: Optional[PropertyAttributes] = Field(alias="attributes", default=None)

    isSpecialName: Optional[bool] = Field(alias="isSpecialName", default=None)

    canRead: Optional[bool] = Field(alias="canRead", default=None)

    canWrite: Optional[bool] = Field(alias="canWrite", default=None)

    getMethod: Optional[MethodInfo] = Field(alias="getMethod", default=None)

    setMethod: Optional[MethodInfo] = Field(alias="setMethod", default=None)
