from typing import *

from pydantic import BaseModel, Field

from .CustomAttributeData import CustomAttributeData
from .MemberTypes import MemberTypes
from .Module import Module
from .Type import Type


class MemberInfo(BaseModel):
    """
    None model

    """

    memberType: Optional[MemberTypes] = Field(alias="memberType", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    declaringType: Optional[Type] = Field(alias="declaringType", default=None)

    reflectedType: Optional[Type] = Field(alias="reflectedType", default=None)

    module: Optional[Module] = Field(alias="module", default=None)

    customAttributes: Optional[List[Optional["CustomAttributeData"]]
                               ] = Field(alias="customAttributes", default=None)

    isCollectible: Optional[bool] = Field(alias="isCollectible", default=None)

    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)
