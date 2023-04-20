from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_curve_segment_type import AbstractCurveSegmentType
from seabeepy.metadata.gmd.curve_interpolation_type import CurveInterpolationType
from seabeepy.metadata.gmd.point_property import PointProperty
from seabeepy.metadata.gmd.pos import Pos
from seabeepy.metadata.gmd.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicStringType(AbstractCurveSegmentType):
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.GEODESIC,
        metadata={
            "type": "Attribute",
        }
    )
