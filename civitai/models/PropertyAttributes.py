from enum import Enum


class PropertyAttributes(str, Enum):

    NONE = "None"
    SPECIALNAME = "SpecialName"
    RTSPECIALNAME = "RTSpecialName"
    HASDEFAULT = "HasDefault"
    RESERVED2 = "Reserved2"
    RESERVED3 = "Reserved3"
    RESERVED4 = "Reserved4"
    RESERVEDMASK = "ReservedMask"
