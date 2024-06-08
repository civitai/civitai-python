from enum import Enum


class JobSupport(str, Enum):

    UNSUPPORTED = "Unsupported"
    UNAVAILABLE = "Unavailable"
    AVAILABLE = "Available"
