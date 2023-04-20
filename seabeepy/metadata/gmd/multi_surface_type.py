from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from seabeepy.metadata.gmd.composite_surface_type import SurfaceMember
from seabeepy.metadata.gmd.surface_members import SurfaceMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface_members: Optional[SurfaceMembers] = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
