from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_general_parameter_value_property_type import (
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from seabeepy.metadata.gmd.abstract_general_transformation_type import AbstractGeneralTransformationType
from seabeepy.metadata.gmd.method import Method
from seabeepy.metadata.gmd.uses_method import UsesMethod

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TransformationType(AbstractGeneralTransformationType):
    uses_method: Optional[UsesMethod] = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method: Optional[Method] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    includes_value: List[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_value: List[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_value: List[ParameterValue2] = field(
        default_factory=list,
        metadata={
            "name": "parameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
