from dataclasses import dataclass
from seabeepy.metadata.gmd.degrees_type import DegreesType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Degrees(DegreesType):
    class Meta:
        name = "degrees"
        namespace = "http://www.opengis.net/gml"
