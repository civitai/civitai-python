from enum import Enum


class ParameterAttributes(str, Enum):

    NONE = "None"
    IN = "In"
    OUT = "Out"
    LCID = "Lcid"
    RETVAL = "Retval"
    OPTIONAL = "Optional"
    HASDEFAULT = "HasDefault"
    HASFIELDMARSHAL = "HasFieldMarshal"
    RESERVED3 = "Reserved3"
    RESERVED4 = "Reserved4"
    RESERVEDMASK = "ReservedMask"
