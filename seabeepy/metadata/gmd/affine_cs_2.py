from dataclasses import dataclass
from seabeepy.metadata.gmd.affine_csproperty_type import AffineCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffineCs2(AffineCspropertyType):
    """
    gml:affineCS is an association role to the affine coordinate system used by
    this CRS.
    """
    class Meta:
        name = "affineCS"
        namespace = "http://www.opengis.net/gml"
