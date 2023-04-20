from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType
from seabeepy.metadata.gmd.coordinates import Coordinates
from seabeepy.metadata.gmd.pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
