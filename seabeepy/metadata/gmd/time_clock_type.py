from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlTime
from seabeepy.metadata.gmd.string_or_ref_type import StringOrRefType
from seabeepy.metadata.gmd.time_calendar_property_type import TimeCalendarPropertyType
from seabeepy.metadata.gmd.time_reference_system_type import TimeReferenceSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeClockType(TimeReferenceSystemType):
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    reference_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "referenceTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    utc_reference: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "utcReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    date_basis: List[TimeCalendarPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateBasis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
