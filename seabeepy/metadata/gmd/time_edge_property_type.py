from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDuration
from seabeepy.metadata.gmd.abstract_time_object_type import AbstractTimeObjectType
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.reference_type import ReferenceType
from seabeepy.metadata.gmd.related_time_type_relative_position import RelatedTimeTypeRelativePosition
from seabeepy.metadata.gmd.show_value import ShowValue
from seabeepy.metadata.gmd.time_interval import TimeInterval
from seabeepy.metadata.gmd.time_position import TimePosition
from seabeepy.metadata.gmd.time_position_type import TimePositionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeEdgePropertyType:
    """
    gml:TimeEdgePropertyType provides for associating a gml:TimeEdge with an
    object.
    """
    time_edge: Optional["TimeEdge"] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeInstantPropertyType:
    """
    gml:TimeInstantPropertyType provides for associating a gml:TimeInstant with
    an object.
    """
    time_instant: Optional["TimeInstant"] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimePrimitivePropertyType:
    """
    gml:TimePrimitivePropertyType provides a standard content model for
    associations between an arbitrary member of the substitution group whose
    head is gml:AbstractTimePrimitive and another object.
    """
    time_edge: Optional["TimeEdge"] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_node: Optional["TimeNode"] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_period: Optional["TimePeriod"] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_instant: Optional["TimeInstant"] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RelatedTimeType(TimePrimitivePropertyType):
    """gml:RelatedTimeType provides a content model for indicating the relative
    position of an arbitrary member of the substitution group whose head is
    gml:AbstractTimePrimitive.

    It extends the generic gml:TimePrimitivePropertyType with an XML
    attribute relativePosition, whose value is selected from the set of
    13 temporal relationships identified by Allen (1983)
    """
    relative_position: Optional[RelatedTimeTypeRelativePosition] = field(
        default=None,
        metadata={
            "name": "relativePosition",
            "type": "Attribute",
        }
    )


@dataclass
class AbstractTimePrimitiveType(AbstractTimeObjectType):
    related_time: List[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbstractTimeGeometricPrimitiveType(AbstractTimePrimitiveType):
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AbstractTimeTopologyPrimitiveType(AbstractTimePrimitiveType):
    complex: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeInstantType(AbstractTimeGeometricPrimitiveType):
    time_position: Optional[TimePosition] = field(
        default=None,
        metadata={
            "name": "timePosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TimeNodeType(AbstractTimeTopologyPrimitiveType):
    previous_edge: List[TimeEdgePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "previousEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    next_edge: List[TimeEdgePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "nextEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    position: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimePeriodType(AbstractTimeGeometricPrimitiveType):
    begin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "beginPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    begin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    end_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "endPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    end: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_interval: Optional[TimeInterval] = field(
        default=None,
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeInstant(TimeInstantType):
    """
    gml:TimeInstant acts as a zero-dimensional geometric primitive that
    represents an identifiable position in time.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNode(TimeNodeType):
    """A time node is a zero-dimensional topological primitive that represents
    an identifiable node in time (it is equivalent to a point in space).

    A node may act as the termination or initiation of any number of
    time edges. A time node may be realised as a geometry, its position,
    whose value is a time instant.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimePeriod(TimePeriodType):
    """gml:TimePeriod acts as a one-dimensional geometric primitive that
    represents an identifiable extent in time.

    The location in of a gml:TimePeriod is described by the temporal
    positions of the instants at which it begins and ends. The length of
    the period is equal to the temporal distance between the two
    bounding temporal positions. Both beginning and end may be described
    in terms of their direct position using gml:TimePositionType which
    is an XML Schema simple content type, or by reference to an
    indentifiable time instant using gml:TimeInstantPropertyType.
    Alternatively a limit of a gml:TimePeriod may use the conventional
    GML property model to make a reference to a time instant described
    elsewhere, or a limit may be indicated as a direct position.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNodePropertyType:
    """
    gml:TimeNodePropertyType provides for associating a gml:TimeNode with an
    object.
    """
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimePeriodPropertyType:
    """
    gml:TimePeriodPropertyType provides for associating a gml:TimePeriod with
    an object.
    """
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TimeEdgeType(AbstractTimeTopologyPrimitiveType):
    start: Optional[TimeNodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    end: Optional[TimeNodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    extent: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TimeEdge(TimeEdgeType):
    """A time edge is a one-dimensional topological primitive.

    It is an open interval that starts and ends at a node. The edge may
    be realised as a geometry whose value is a time period.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
