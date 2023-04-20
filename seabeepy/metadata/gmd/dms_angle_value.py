from dataclasses import dataclass
from seabeepy.metadata.gmd.dmsangle_type import DmsangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsAngleValue(DmsangleType):
    class Meta:
        name = "dmsAngleValue"
        namespace = "http://www.opengis.net/gml"
