from typing import *

from pydantic import BaseModel, Field

from .CustomAttributeTypedArgument import CustomAttributeTypedArgument
from .MemberInfo import MemberInfo


class CustomAttributeNamedArgument(BaseModel):
    """
    None model

    """

    memberInfo: Optional[MemberInfo] = Field(alias="memberInfo", default=None)

    typedValue: Optional[CustomAttributeTypedArgument] = Field(alias="typedValue", default=None)

    memberName: Optional[str] = Field(alias="memberName", default=None)

    isField: Optional[bool] = Field(alias="isField", default=None)
