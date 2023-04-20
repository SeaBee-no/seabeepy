from dataclasses import dataclass
from seabeepy.metadata.gmd.cartesian_csproperty_type import CartesianCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCs2(CartesianCspropertyType):
    """
    gml:cartesianCS is an association role to the Cartesian coordinate system
    used by this CRS.
    """
    class Meta:
        name = "cartesianCS"
        namespace = "http://www.opengis.net/gml"
