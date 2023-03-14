from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_general_operation_parameter_property_type import (
    GeneralOperationParameter,
    UsesParameter,
)
from seabeepy.metadata.gmd.formula import Formula
from seabeepy.metadata.gmd.identified_object_type import IdentifiedObjectType
from seabeepy.metadata.gmd.method_formula import MethodFormula

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodType(IdentifiedObjectType):
    method_formula: Optional[MethodFormula] = field(
        default=None,
        metadata={
            "name": "methodFormula",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    formula: Optional[Formula] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    source_dimensions: Optional[int] = field(
        default=None,
        metadata={
            "name": "sourceDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    target_dimensions: Optional[int] = field(
        default=None,
        metadata={
            "name": "targetDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_parameter: List[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    general_operation_parameter: List[GeneralOperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "generalOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
