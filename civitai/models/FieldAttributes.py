from enum import Enum


class FieldAttributes(str, Enum):

    PRIVATESCOPE = "PrivateScope"
    PRIVATE = "Private"
    FAMANDASSEM = "FamANDAssem"
    ASSEMBLY = "Assembly"
    FAMILY = "Family"
    FAMORASSEM = "FamORAssem"
    PUBLIC = "Public"
    FIELDACCESSMASK = "FieldAccessMask"
    STATIC = "Static"
    INITONLY = "InitOnly"
    LITERAL = "Literal"
    NOTSERIALIZED = "NotSerialized"
    HASFIELDRVA = "HasFieldRVA"
    SPECIALNAME = "SpecialName"
    RTSPECIALNAME = "RTSpecialName"
    HASFIELDMARSHAL = "HasFieldMarshal"
    PINVOKEIMPL = "PinvokeImpl"
    HASDEFAULT = "HasDefault"
    RESERVEDMASK = "ReservedMask"
