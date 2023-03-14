from dataclasses import dataclass
from seabeepy.metadata.gmd.ellipsoid_property_type import EllipsoidPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidRef(EllipsoidPropertyType):
    class Meta:
        name = "ellipsoidRef"
        namespace = "http://www.opengis.net/gml"
