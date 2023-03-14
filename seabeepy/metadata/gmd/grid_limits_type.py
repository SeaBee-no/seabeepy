from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.grid_envelope_type import GridEnvelopeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridLimitsType:
    grid_envelope: Optional[GridEnvelopeType] = field(
        default=None,
        metadata={
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
