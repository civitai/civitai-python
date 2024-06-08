from enum import Enum


class LayoutKind(str, Enum):

    SEQUENTIAL = "Sequential"
    EXPLICIT = "Explicit"
    AUTO = "Auto"
