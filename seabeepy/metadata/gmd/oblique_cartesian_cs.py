from dataclasses import dataclass
from seabeepy.metadata.gmd.oblique_cartesian_cstype import ObliqueCartesianCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ObliqueCartesianCs(ObliqueCartesianCstype):
    class Meta:
        name = "ObliqueCartesianCS"
        namespace = "http://www.opengis.net/gml"
