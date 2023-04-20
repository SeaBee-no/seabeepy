from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from seabeepy.metadata.gmd.composite_curve_type import CurveMember
from seabeepy.metadata.gmd.curve_members import CurveMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    curve_members: Optional[CurveMembers] = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
