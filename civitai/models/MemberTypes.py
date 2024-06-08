from enum import Enum


class MemberTypes(str, Enum):

    CONSTRUCTOR = "Constructor"
    EVENT = "Event"
    FIELD = "Field"
    METHOD = "Method"
    PROPERTY = "Property"
    TYPEINFO = "TypeInfo"
    CUSTOM = "Custom"
    NESTEDTYPE = "NestedType"
    ALL = "All"
