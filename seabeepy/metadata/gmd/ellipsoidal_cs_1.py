from dataclasses import dataclass
from seabeepy.metadata.gmd.ellipsoidal_cstype import EllipsoidalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCs1(EllipsoidalCstype):
    """gml:EllipsoidalCS is a two- or three-dimensional coordinate system in
    which position is specified by geodetic latitude, geodetic longitude, and
    (in the three-dimensional case) ellipsoidal height.

    An EllipsoidalCS shall have two or three gml:axis property elements;
    the number of associations shall equal the dimension of the CS.
    """
    class Meta:
        name = "EllipsoidalCS"
        namespace = "http://www.opengis.net/gml"
