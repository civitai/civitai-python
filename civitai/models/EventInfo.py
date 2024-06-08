from typing import *

from pydantic import BaseModel, Field

from .CustomAttributeData import CustomAttributeData
from .EventAttributes import EventAttributes
from .MemberTypes import MemberTypes
from .MethodInfo import MethodInfo
from .Module import Module
from .Type import Type


class EventInfo(BaseModel):
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

    attributes: Optional[EventAttributes] = Field(alias="attributes", default=None)

    isSpecialName: Optional[bool] = Field(alias="isSpecialName", default=None)

    addMethod: Optional[MethodInfo] = Field(alias="addMethod", default=None)

    removeMethod: Optional[MethodInfo] = Field(alias="removeMethod", default=None)

    raiseMethod: Optional[MethodInfo] = Field(alias="raiseMethod", default=None)

    isMulticast: Optional[bool] = Field(alias="isMulticast", default=None)

    eventHandlerType: Optional[Type] = Field(alias="eventHandlerType", default=None)
