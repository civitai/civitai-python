from typing import *

from pydantic import BaseModel, Field

from .CustomAttributeData import CustomAttributeData
from .FieldAttributes import FieldAttributes
from .MemberTypes import MemberTypes
from .Module import Module
from .RuntimeFieldHandle import RuntimeFieldHandle
from .Type import Type


class FieldInfo(BaseModel):
    """
    None model

    """

    name: Optional[str] = Field(alias="name", default=None)

    declaringType: Optional[Type] = Field(alias="declaringType", default=None)

    reflectedType: Optional[Type] = Field(alias="reflectedType", default=None)

    module: Optional[Module] = Field(alias="module", default=None)

    customAttributes: Optional[List[Optional["CustomAttributeData"]]
                               ] = Field(alias="customAttributes", default=None)

    isCollectible: Optional[bool] = Field(alias="isCollectible", default=None)

    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)

    memberType: Optional[MemberTypes] = Field(alias="memberType", default=None)

    attributes: Optional[FieldAttributes] = Field(alias="attributes", default=None)

    fieldType: Optional[Type] = Field(alias="fieldType", default=None)

    isInitOnly: Optional[bool] = Field(alias="isInitOnly", default=None)

    isLiteral: Optional[bool] = Field(alias="isLiteral", default=None)

    isPinvokeImpl: Optional[bool] = Field(alias="isPinvokeImpl", default=None)

    isSpecialName: Optional[bool] = Field(alias="isSpecialName", default=None)

    isStatic: Optional[bool] = Field(alias="isStatic", default=None)

    isAssembly: Optional[bool] = Field(alias="isAssembly", default=None)

    isFamily: Optional[bool] = Field(alias="isFamily", default=None)

    isFamilyAndAssembly: Optional[bool] = Field(alias="isFamilyAndAssembly", default=None)

    isFamilyOrAssembly: Optional[bool] = Field(alias="isFamilyOrAssembly", default=None)

    isPrivate: Optional[bool] = Field(alias="isPrivate", default=None)

    isPublic: Optional[bool] = Field(alias="isPublic", default=None)

    isSecurityCritical: Optional[bool] = Field(alias="isSecurityCritical", default=None)

    isSecuritySafeCritical: Optional[bool] = Field(alias="isSecuritySafeCritical", default=None)

    isSecurityTransparent: Optional[bool] = Field(alias="isSecurityTransparent", default=None)

    fieldHandle: Optional[RuntimeFieldHandle] = Field(alias="fieldHandle", default=None)
