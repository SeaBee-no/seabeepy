from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from xsdata.models.datatype import XmlDate, XmlPeriod
from seabeepy.metadata.gmd.definition_type import DefinitionType
from seabeepy.metadata.gmd.string_or_ref_type import StringOrRefType
from seabeepy.metadata.gmd.time_edge_property_type import TimePeriodPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCalendarEraType(DefinitionType):
    reference_event: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "referenceEvent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    reference_date: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "name": "referenceDate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    julian_reference: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "julianReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    epoch_of_use: Optional[TimePeriodPropertyType] = field(
        default=None,
        metadata={
            "name": "epochOfUse",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
