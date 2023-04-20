from dataclasses import dataclass
from seabeepy.metadata.gmd.point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Point(PointType):
    """A Point is defined by a single coordinate tuple.

    The direct position of a point is specified by the pos element which
    is of type DirectPositionType.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
