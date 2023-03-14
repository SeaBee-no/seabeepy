from dataclasses import dataclass
from seabeepy.metadata.gmd.cartesian_csproperty_type import CartesianCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCartesianCs(CartesianCspropertyType):
    class Meta:
        name = "usesCartesianCS"
        namespace = "http://www.opengis.net/gml"
