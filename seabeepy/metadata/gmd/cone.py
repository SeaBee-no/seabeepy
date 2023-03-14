from dataclasses import dataclass
from seabeepy.metadata.gmd.cone_type import ConeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
