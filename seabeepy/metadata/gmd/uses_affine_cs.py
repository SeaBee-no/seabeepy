from dataclasses import dataclass
from seabeepy.metadata.gmd.affine_csproperty_type import AffineCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesAffineCs(AffineCspropertyType):
    class Meta:
        name = "usesAffineCS"
        namespace = "http://www.opengis.net/gml"
