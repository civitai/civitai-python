from enum import Enum


class SecurityRuleSet(str, Enum):

    NONE = "None"
    LEVEL1 = "Level1"
    LEVEL2 = "Level2"
