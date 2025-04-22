from typing import *

from pydantic import BaseModel, Field

from .Assembly import Assembly
from .CustomAttributeData import CustomAttributeData
from .ModuleHandle import ModuleHandle


class Module(BaseModel):
    """
    None model

    """

    assembly: Optional[Assembly] = Field(alias="assembly", default=None)

    fullyQualifiedName: Optional[str] = Field(alias="fullyQualifiedName", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    mdStreamVersion: Optional[int] = Field(alias="mdStreamVersion", default=None)

    moduleVersionId: Optional[str] = Field(alias="moduleVersionId", default=None)

    scopeName: Optional[str] = Field(alias="scopeName", default=None)

    moduleHandle: Optional[ModuleHandle] = Field(alias="moduleHandle", default=None)

    customAttributes: Optional[List[Optional[CustomAttributeData]]] = Field(alias="customAttributes", default=None)

    metadataToken: Optional[int] = Field(alias="metadataToken", default=None)
