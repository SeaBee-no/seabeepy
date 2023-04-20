from dataclasses import dataclass
from seabeepy.metadata.gmd.ellipsoidal_csproperty_type import EllipsoidalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCs2(EllipsoidalCspropertyType):
    """
    gml:ellipsoidalCS is an association role to the ellipsoidal coordinate
    system used by this CRS.
    """
    class Meta:
        name = "ellipsoidalCS"
        namespace = "http://www.opengis.net/gml"
