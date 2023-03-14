from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.time_edge_property_type import TimeInstantPropertyType
from seabeepy.metadata.gmd.time_interval_length_type import TimeIntervalLengthType
from seabeepy.metadata.gmd.time_position_type import TimePositionType
from seabeepy.metadata.gmd.time_reference_system_type import TimeReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystemType(TimeReferenceSystemType):
    origin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    origin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interval: Optional[TimeIntervalLengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
