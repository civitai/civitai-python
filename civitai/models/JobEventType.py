from enum import Enum


class JobEventType(str, Enum):

    INITIALIZED = "Initialized"
    CLAIMED = "Claimed"
    REJECTED = "Rejected"
    LATEREJECTED = "LateRejected"
    CLAIMEXPIRED = "ClaimExpired"
    UPDATED = "Updated"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    EXPIRED = "Expired"
    DELETED = "Deleted"
