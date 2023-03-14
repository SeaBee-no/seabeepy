from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.direct_position_type import DirectPositionType
from seabeepy.metadata.gmd.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffinePlacementType:
    location: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    ref_direction: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    in_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "inDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    out_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "outDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
