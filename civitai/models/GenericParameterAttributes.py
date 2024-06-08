from enum import Enum


class GenericParameterAttributes(str, Enum):

    NONE = "None"
    COVARIANT = "Covariant"
    CONTRAVARIANT = "Contravariant"
    VARIANCEMASK = "VarianceMask"
    REFERENCETYPECONSTRAINT = "ReferenceTypeConstraint"
    NOTNULLABLEVALUETYPECONSTRAINT = "NotNullableValueTypeConstraint"
    DEFAULTCONSTRUCTORCONSTRAINT = "DefaultConstructorConstraint"
    SPECIALCONSTRAINTMASK = "SpecialConstraintMask"
