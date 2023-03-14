from dataclasses import dataclass
from seabeepy.metadata.gmd.spherical_csproperty_type import SphericalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCs2(SphericalCspropertyType):
    """
    gml:sphericalCS is an association role to the spherical coordinate system
    used by this CRS.
    """
    class Meta:
        name = "sphericalCS"
        namespace = "http://www.opengis.net/gml"
