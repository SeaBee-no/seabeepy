from dataclasses import dataclass
from seabeepy.metadata.gmd.bounding_shape_type import BoundingShapeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundedBy(BoundingShapeType):
    """
    This property describes the minimum bounding box or rectangle that encloses
    the entire feature.
    """
    class Meta:
        name = "boundedBy"
        nillable = True
        namespace = "http://www.opengis.net/gml"
