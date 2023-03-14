from dataclasses import dataclass
from seabeepy.metadata.gmd.oblique_cartesian_csproperty_type import ObliqueCartesianCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesObliqueCartesianCs(ObliqueCartesianCspropertyType):
    class Meta:
        name = "usesObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml"
