from typing import *

from pydantic import BaseModel, Field

class Assembly(BaseModel):
    """
    None model

    """

    definedTypes: Optional[List[Optional["TypeInfo"]]] = Field(alias="definedTypes", default=None)

    exportedTypes: Optional[List[Optional["Type"]]] = Field(alias="exportedTypes", default=None)

    entryPoint: Optional["MethodInfo"] = Field(alias="entryPoint", default=None)

    fullName: Optional[str] = Field(alias="fullName", default=None)

    imageRuntimeVersion: Optional[str] = Field(alias="imageRuntimeVersion", default=None)

    isDynamic: Optional[bool] = Field(alias="isDynamic", default=None)

    location: Optional[str] = Field(alias="location", default=None)

    reflectionOnly: Optional[bool] = Field(alias="reflectionOnly", default=None)

    isCollectible: Optional[bool] = Field(alias="isCollectible", default=None)

    isFullyTrusted: Optional[bool] = Field(alias="isFullyTrusted", default=None)

    customAttributes: Optional[List[Optional["CustomAttributeData"]]] = Field(alias="customAttributes", default=None)

    manifestModule: Optional["Module"] = Field(alias="manifestModule", default=None)

    modules: Optional[List[Optional["Module"]]] = Field(alias="modules", default=None)

    hostContext: Optional[int] = Field(alias="hostContext", default=None)

    securityRuleSet: Optional["SecurityRuleSet"] = Field(alias="securityRuleSet", default=None)

    class Config:
        arbitrary_types_allowed = True

from .CustomAttributeData import CustomAttributeData
from .MethodInfo import MethodInfo
from .Module import Module
from .SecurityRuleSet import SecurityRuleSet
from .Type import Type
from .TypeInfo import TypeInfo