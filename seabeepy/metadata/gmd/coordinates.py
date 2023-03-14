from dataclasses import dataclass
from seabeepy.metadata.gmd.coordinates_type import CoordinatesType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Coordinates(CoordinatesType):
    class Meta:
        name = "coordinates"
        namespace = "http://www.opengis.net/gml"
