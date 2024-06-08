from enum import Enum


class WorkerAssetAvailability(str, Enum):

    UNKNOWN = "Unknown"
    UNSUPPORTED = "Unsupported"
    UNAVAILABLE = "Unavailable"
    AVAILABLE = "Available"
