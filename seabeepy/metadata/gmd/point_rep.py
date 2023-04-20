from dataclasses import dataclass
from seabeepy.metadata.gmd.point_property_type import PointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointRep(PointPropertyType):
    class Meta:
        name = "pointRep"
        namespace = "http://www.opengis.net/gml"
