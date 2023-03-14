from dataclasses import dataclass
from seabeepy.metadata.gmd.coordinate_system_property_type import CoordinateSystemPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCs(CoordinateSystemPropertyType):
    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml"
