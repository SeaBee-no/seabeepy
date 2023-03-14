from dataclasses import dataclass
from seabeepy.metadata.gmd.sphere_type import SphereType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Sphere(SphereType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
