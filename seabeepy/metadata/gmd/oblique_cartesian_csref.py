from dataclasses import dataclass
from seabeepy.metadata.gmd.oblique_cartesian_csproperty_type import ObliqueCartesianCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCsref(ObliqueCartesianCspropertyType):
    class Meta:
        name = "obliqueCartesianCSRef"
        namespace = "http://www.opengis.net/gml"
