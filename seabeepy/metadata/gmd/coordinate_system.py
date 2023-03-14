from dataclasses import dataclass
from seabeepy.metadata.gmd.coordinate_system_property_type import CoordinateSystemPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystem(CoordinateSystemPropertyType):
    """
    An association role to the coordinate system used by this CRS.
    """
    class Meta:
        name = "coordinateSystem"
        namespace = "http://www.opengis.net/gml"
