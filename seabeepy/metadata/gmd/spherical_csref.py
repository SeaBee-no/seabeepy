from dataclasses import dataclass
from seabeepy.metadata.gmd.spherical_csproperty_type import SphericalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCsref(SphericalCspropertyType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml"
