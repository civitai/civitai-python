from enum import Enum


class MethodAttributes(str, Enum):

    PRIVATESCOPE = "PrivateScope"
    PRIVATE = "Private"
    FAMANDASSEM = "FamANDAssem"
    ASSEMBLY = "Assembly"
    FAMILY = "Family"
    FAMORASSEM = "FamORAssem"
    PUBLIC = "Public"
    MEMBERACCESSMASK = "MemberAccessMask"
    UNMANAGEDEXPORT = "UnmanagedExport"
    STATIC = "Static"
    FINAL = "Final"
    VIRTUAL = "Virtual"
    HIDEBYSIG = "HideBySig"
    NEWSLOT = "NewSlot"
    CHECKACCESSONOVERRIDE = "CheckAccessOnOverride"
    ABSTRACT = "Abstract"
    SPECIALNAME = "SpecialName"
    RTSPECIALNAME = "RTSpecialName"
    PINVOKEIMPL = "PinvokeImpl"
    HASSECURITY = "HasSecurity"
    REQUIRESECOBJECT = "RequireSecObject"
    RESERVEDMASK = "ReservedMask"
