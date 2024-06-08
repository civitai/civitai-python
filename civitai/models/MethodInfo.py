from typing import *

from pydantic import BaseModel, Field

from .CallingConventions import CallingConventions
from .CustomAttributeData import CustomAttributeData
from .ICustomAttributeProvider import ICustomAttributeProvider
from .MemberTypes import MemberTypes
from .MethodAttributes import MethodAttributes
from .MethodImplAttributes import MethodImplAttributes
from .Module import Module
from .ParameterInfo import ParameterInfo
from .RuntimeMethodHandle import RuntimeMethodHandle
from .Type import Type


class MethodInfo(BaseModel):
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

    attributes: Optional[MethodAttributes] = Field(alias="attributes", default=None)

    methodImplementationFlags: Optional[MethodImplAttributes] = Field(alias="methodImplementationFlags", default=None)

    callingConvention: Optional[CallingConventions] = Field(alias="callingConvention", default=None)

    isAbstract: Optional[bool] = Field(alias="isAbstract", default=None)

    isConstructor: Optional[bool] = Field(alias="isConstructor", default=None)

    isFinal: Optional[bool] = Field(alias="isFinal", default=None)

    isHideBySig: Optional[bool] = Field(alias="isHideBySig", default=None)

    isSpecialName: Optional[bool] = Field(alias="isSpecialName", default=None)

    isStatic: Optional[bool] = Field(alias="isStatic", default=None)

    isVirtual: Optional[bool] = Field(alias="isVirtual", default=None)

    isAssembly: Optional[bool] = Field(alias="isAssembly", default=None)

    isFamily: Optional[bool] = Field(alias="isFamily", default=None)

    isFamilyAndAssembly: Optional[bool] = Field(alias="isFamilyAndAssembly", default=None)

    isFamilyOrAssembly: Optional[bool] = Field(alias="isFamilyOrAssembly", default=None)

    isPrivate: Optional[bool] = Field(alias="isPrivate", default=None)

    isPublic: Optional[bool] = Field(alias="isPublic", default=None)

    isConstructedGenericMethod: Optional[bool] = Field(alias="isConstructedGenericMethod", default=None)

    isGenericMethod: Optional[bool] = Field(alias="isGenericMethod", default=None)

    isGenericMethodDefinition: Optional[bool] = Field(alias="isGenericMethodDefinition", default=None)

    containsGenericParameters: Optional[bool] = Field(alias="containsGenericParameters", default=None)

    methodHandle: Optional[RuntimeMethodHandle] = Field(alias="methodHandle", default=None)

    isSecurityCritical: Optional[bool] = Field(alias="isSecurityCritical", default=None)

    isSecuritySafeCritical: Optional[bool] = Field(alias="isSecuritySafeCritical", default=None)

    isSecurityTransparent: Optional[bool] = Field(alias="isSecurityTransparent", default=None)

    memberType: Optional[MemberTypes] = Field(alias="memberType", default=None)

    returnParameter: Optional[ParameterInfo] = Field(alias="returnParameter", default=None)

    returnType: Optional[Type] = Field(alias="returnType", default=None)

    returnTypeCustomAttributes: Optional[ICustomAttributeProvider] = Field(
        alias="returnTypeCustomAttributes", default=None
    )
