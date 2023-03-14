from dataclasses import dataclass
from seabeepy.metadata.gmd.ex_bounding_polygon_type import ExBoundingPolygonType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExBoundingPolygon(ExBoundingPolygonType):
    class Meta:
        name = "EX_BoundingPolygon"
        namespace = "http://www.isotc211.org/2005/gmd"
