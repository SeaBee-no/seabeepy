from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_surface_type import AbstractSurfaceType
from seabeepy.metadata.gmd.exterior import Exterior
from seabeepy.metadata.gmd.interior import Interior

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonType(AbstractSurfaceType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interior: List[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
