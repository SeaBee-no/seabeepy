from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_ring_type import AbstractRingType
from seabeepy.metadata.gmd.coordinates import Coordinates
from seabeepy.metadata.gmd.point_property import PointProperty
from seabeepy.metadata.gmd.point_rep import PointRep
from seabeepy.metadata.gmd.pos import Pos
from seabeepy.metadata.gmd.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRingType(AbstractRingType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    point_rep: List[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 4,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
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
