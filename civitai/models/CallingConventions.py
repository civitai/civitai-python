from enum import Enum


class CallingConventions(str, Enum):

    STANDARD = "Standard"
    VARARGS = "VarArgs"
    ANY = "Any"
    HASTHIS = "HasThis"
    EXPLICITTHIS = "ExplicitThis"
