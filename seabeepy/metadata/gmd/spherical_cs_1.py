from dataclasses import dataclass
from seabeepy.metadata.gmd.spherical_cstype import SphericalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCs1(SphericalCstype):
    """gml:SphericalCS is a three-dimensional coordinate system with one
    distance measured from the origin and two angular coordinates.

    A SphericalCS shall have three gml:axis property elements.
    """
    class Meta:
        name = "SphericalCS"
        namespace = "http://www.opengis.net/gml"
