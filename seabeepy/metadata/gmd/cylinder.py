from dataclasses import dataclass
from seabeepy.metadata.gmd.cylinder_type import CylinderType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
