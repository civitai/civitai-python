from enum import Enum


class MethodImplAttributes(str, Enum):

    IL = "IL"
    NATIVE = "Native"
    OPTIL = "OPTIL"
    CODETYPEMASK = "CodeTypeMask"
    MANAGEDMASK = "ManagedMask"
    NOINLINING = "NoInlining"
    FORWARDREF = "ForwardRef"
    SYNCHRONIZED = "Synchronized"
    NOOPTIMIZATION = "NoOptimization"
    PRESERVESIG = "PreserveSig"
    AGGRESSIVEINLINING = "AggressiveInlining"
    AGGRESSIVEOPTIMIZATION = "AggressiveOptimization"
    INTERNALCALL = "InternalCall"
    MAXMETHODIMPLVAL = "MaxMethodImplVal"
