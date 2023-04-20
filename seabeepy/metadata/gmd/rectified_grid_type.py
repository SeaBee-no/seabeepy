from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.grid_type import GridType
from seabeepy.metadata.gmd.point_property_type import PointPropertyType
from seabeepy.metadata.gmd.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridType(GridType):
    origin: Optional[PointPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    offset_vector: List[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "offsetVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
