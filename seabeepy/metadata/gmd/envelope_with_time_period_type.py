from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.envelope_type import EnvelopeType
from seabeepy.metadata.gmd.time_position_type import TimePositionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriodType(EnvelopeType):
    begin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "beginPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    end_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "endPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        }
    )
