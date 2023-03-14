from dataclasses import dataclass
from seabeepy.metadata.gmd.affine_cstype import AffineCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffineCs1(AffineCstype):
    """gml:AffineCS is a two- or three-dimensional coordinate system with
    straight axes that are not necessarily orthogonal.

    An AffineCS shall have two or three gml:axis property elements; the
    number of property elements shall equal the dimension of the CS.
    """
    class Meta:
        name = "AffineCS"
        namespace = "http://www.opengis.net/gml"
