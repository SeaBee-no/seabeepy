from dataclasses import dataclass, field
from typing import List, Optional, Union
from seabeepy.metadata.gmd.abstract_general_operation_parameter_type import AbstractGeneralOperationParameterType
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.operation_parameter_1 import OperationParameter1
from seabeepy.metadata.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterPropertyType:
    """
    gml:AbstractGeneralOperationParameterPropertyType is a property type for
    association roles to an operation parameter or group, either referencing or
    containing the definition of that parameter or group.
    """
    operation_parameter_group: Optional["OperationParameterGroup"] = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    operation_parameter: Optional[OperationParameter1] = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeneralOperationParameter(AbstractGeneralOperationParameterPropertyType):
    """
    gml:generalOperationParameter is an association to an operation parameter
    or parameter group.
    """
    class Meta:
        name = "generalOperationParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "usesParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupType(AbstractGeneralOperationParameterType):
    maximum_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "maximumOccurs",
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


@dataclass
class OperationParameterGroup(OperationParameterGroupType):
    """gml:OperationParameterGroup is the definition of a group of parameters
    used by an operation method.

    This complex type is expected to be used or extended for all
    applicable operation methods, without defining operation-method-
    specialized element names. The generalOperationParameter elements
    are an unordered list of associations to the set of operation
    parameters that are members of this group.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
