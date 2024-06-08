from enum import Enum


class ModelValidationState(str, Enum):

    UNVALIDATED = "Unvalidated"
    INVALID = "Invalid"
    VALID = "Valid"
    SKIPPED = "Skipped"
