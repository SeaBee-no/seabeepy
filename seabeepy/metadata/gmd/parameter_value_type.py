from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_general_parameter_value_type import AbstractGeneralParameterValueType
from seabeepy.metadata.gmd.dms_angle_value import DmsAngleValue
from seabeepy.metadata.gmd.operation_parameter_2 import OperationParameter2
from seabeepy.metadata.gmd.value import Value
from seabeepy.metadata.gmd.value_list import ValueList
from seabeepy.metadata.gmd.value_of_parameter import ValueOfParameter

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValueType(AbstractGeneralParameterValueType):
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    dms_angle_value: Optional[DmsAngleValue] = field(
        default=None,
        metadata={
            "name": "dmsAngleValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    string_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    integer_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    boolean_value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    value_list: Optional[ValueList] = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    integer_value_list: List[int] = field(
        default_factory=list,
        metadata={
            "name": "integerValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        }
    )
    value_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueFile",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    value_of_parameter: Optional[ValueOfParameter] = field(
        default=None,
        metadata={
            "name": "valueOfParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation_parameter: Optional[OperationParameter2] = field(
        default=None,
        metadata={
            "name": "operationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
