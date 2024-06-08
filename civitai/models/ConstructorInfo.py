from typing import *

from pydantic import BaseModel, Field

class ConstructorInfo(BaseModel):
    """
    None model
    """

    name: Optional[str] = Field(alias="name", default=None)
    declaringType: Optional["Type"] = Field(alias="declaringType", default=None)
    reflectedType: Optional["Type"] = Field(alias="reflectedType", default=None)
    module: Optional["Module"] = Field(alias="module", default=None)
    customAttributes: Optional[List[Optional["CustomAttributeData"]]] = Field(alias="customAttributes", default=None)
    isCollectible: Optional[bool] = Field(alias="isCollectible", default=None)
    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)
    attributes: Optional["MethodAttributes"] = Field(alias="attributes", default=None)
    methodImplementationFlags: Optional["MethodImplAttributes"] = Field(alias="methodImplementationFlags", default=None)
    callingConvention: Optional["CallingConventions"] = Field(alias="callingConvention", default=None)
    isAbstract: Optional[bool] = Field(alias="isAbstract", default=None)
    isConstructor: Optional[bool] = Field(alias="isConstructor", default=None)
    isFinal: Optional[bool] = Field(alias="isFinal", default=None)

    class Config:
        arbitrary_types_allowed = True

from .CallingConventions import CallingConventions
from .CustomAttributeData import CustomAttributeData
from .MemberTypes import MemberTypes
from .MethodAttributes import MethodAttributes
from .MethodImplAttributes import MethodImplAttributes
from .Module import Module
from .Type import Type