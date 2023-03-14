from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.aggregation_type import AggregationType
from seabeepy.metadata.gmd.composite_surface_type import SurfaceMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ShellType:
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
