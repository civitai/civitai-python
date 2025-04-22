from typing import *

from pydantic import BaseModel, Field

from .Assembly import Assembly
from .ConstructorInfo import ConstructorInfo
from .CustomAttributeData import CustomAttributeData
from .GenericParameterAttributes import GenericParameterAttributes
from .MemberTypes import MemberTypes
from .MethodBase import MethodBase
from .Module import Module
from .RuntimeTypeHandle import RuntimeTypeHandle
from .StructLayoutAttribute import StructLayoutAttribute
from .TypeAttributes import TypeAttributes


class Type(BaseModel):
    """
    None model

    """

    name: Optional[str] = Field(alias="name", default=None)

    customAttributes: Optional[List[Optional[CustomAttributeData]]
                               ] = Field(alias="customAttributes", default=None)

    isCollectible: Optional[bool] = Field(alias="isCollectible", default=None)

    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)

    isInterface: Optional[bool] = Field(alias="isInterface", default=None)

    memberType: Optional[MemberTypes] = Field(alias="memberType", default=None)

    namespace: Optional[str] = Field(alias="namespace", default=None)

    assemblyQualifiedName: Optional[str] = Field(alias="assemblyQualifiedName", default=None)

    fullName: Optional[str] = Field(alias="fullName", default=None)

    assembly: Optional[Assembly] = Field(alias="assembly", default=None)

    module: Optional[Module] = Field(alias="module", default=None)

    isNested: Optional[bool] = Field(alias="isNested", default=None)

    declaringType: Optional["Type"] = Field(alias="declaringType", default=None)

    declaringMethod: Optional[MethodBase] = Field(alias="declaringMethod", default=None)

    reflectedType: Optional["Type"] = Field(alias="reflectedType", default=None)

    underlyingSystemType: Optional["Type"] = Field(alias="underlyingSystemType", default=None)

    isTypeDefinition: Optional[bool] = Field(alias="isTypeDefinition", default=None)

    isArray: Optional[bool] = Field(alias="isArray", default=None)

    isByRef: Optional[bool] = Field(alias="isByRef", default=None)

    isPointer: Optional[bool] = Field(alias="isPointer", default=None)

    isConstructedGenericType: Optional[bool] = Field(
        alias="isConstructedGenericType", default=None)

    isGenericParameter: Optional[bool] = Field(alias="isGenericParameter", default=None)

    isGenericTypeParameter: Optional[bool] = Field(alias="isGenericTypeParameter", default=None)

    isGenericMethodParameter: Optional[bool] = Field(
        alias="isGenericMethodParameter", default=None)

    isGenericType: Optional[bool] = Field(alias="isGenericType", default=None)

    isGenericTypeDefinition: Optional[bool] = Field(alias="isGenericTypeDefinition", default=None)

    isSZArray: Optional[bool] = Field(alias="isSZArray", default=None)

    isVariableBoundArray: Optional[bool] = Field(alias="isVariableBoundArray", default=None)

    isByRefLike: Optional[bool] = Field(alias="isByRefLike", default=None)

    isFunctionPointer: Optional[bool] = Field(alias="isFunctionPointer", default=None)

    isUnmanagedFunctionPointer: Optional[bool] = Field(
        alias="isUnmanagedFunctionPointer", default=None)

    hasElementType: Optional[bool] = Field(alias="hasElementType", default=None)

    genericTypeArguments: Optional[List[Optional["Type"]]] = Field(
        alias="genericTypeArguments", default=None)

    genericParameterPosition: Optional[int] = Field(alias="genericParameterPosition", default=None)

    genericParameterAttributes: Optional[GenericParameterAttributes] = Field(
        alias="genericParameterAttributes", default=None
    )

    attributes: Optional[TypeAttributes] = Field(alias="attributes", default=None)

    isAbstract: Optional[bool] = Field(alias="isAbstract", default=None)

    isImport: Optional[bool] = Field(alias="isImport", default=None)

    isSealed: Optional[bool] = Field(alias="isSealed", default=None)

    isSpecialName: Optional[bool] = Field(alias="isSpecialName", default=None)

    isClass: Optional[bool] = Field(alias="isClass", default=None)

    isNestedAssembly: Optional[bool] = Field(alias="isNestedAssembly", default=None)

    isNestedFamANDAssem: Optional[bool] = Field(alias="isNestedFamANDAssem", default=None)

    isNestedFamily: Optional[bool] = Field(alias="isNestedFamily", default=None)

    isNestedFamORAssem: Optional[bool] = Field(alias="isNestedFamORAssem", default=None)

    isNestedPrivate: Optional[bool] = Field(alias="isNestedPrivate", default=None)

    isNestedPublic: Optional[bool] = Field(alias="isNestedPublic", default=None)

    isNotPublic: Optional[bool] = Field(alias="isNotPublic", default=None)

    isPublic: Optional[bool] = Field(alias="isPublic", default=None)

    isAutoLayout: Optional[bool] = Field(alias="isAutoLayout", default=None)

    isExplicitLayout: Optional[bool] = Field(alias="isExplicitLayout", default=None)

    isLayoutSequential: Optional[bool] = Field(alias="isLayoutSequential", default=None)

    isAnsiClass: Optional[bool] = Field(alias="isAnsiClass", default=None)

    isAutoClass: Optional[bool] = Field(alias="isAutoClass", default=None)

    isUnicodeClass: Optional[bool] = Field(alias="isUnicodeClass", default=None)

    isCOMObject: Optional[bool] = Field(alias="isCOMObject", default=None)

    isContextful: Optional[bool] = Field(alias="isContextful", default=None)

    isEnum: Optional[bool] = Field(alias="isEnum", default=None)

    isMarshalByRef: Optional[bool] = Field(alias="isMarshalByRef", default=None)

    isPrimitive: Optional[bool] = Field(alias="isPrimitive", default=None)

    isValueType: Optional[bool] = Field(alias="isValueType", default=None)

    isSignatureType: Optional[bool] = Field(alias="isSignatureType", default=None)

    isSecurityCritical: Optional[bool] = Field(alias="isSecurityCritical", default=None)

    isSecuritySafeCritical: Optional[bool] = Field(alias="isSecuritySafeCritical", default=None)

    isSecurityTransparent: Optional[bool] = Field(alias="isSecurityTransparent", default=None)

    structLayoutAttribute: Optional[StructLayoutAttribute] = Field(
        alias="structLayoutAttribute", default=None)

    typeInitializer: Optional[ConstructorInfo] = Field(alias="typeInitializer", default=None)

    typeHandle: Optional[RuntimeTypeHandle] = Field(alias="typeHandle", default=None)

    guid: Optional[str] = Field(alias="guid", default=None)

    baseType: Optional["Type"] = Field(alias="baseType", default=None)

    containsGenericParameters: Optional[bool] = Field(
        alias="containsGenericParameters", default=None)

    isVisible: Optional[bool] = Field(alias="isVisible", default=None)
