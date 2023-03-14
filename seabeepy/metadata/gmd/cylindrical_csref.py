from dataclasses import dataclass
from seabeepy.metadata.gmd.cylindrical_csproperty_type import CylindricalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCsref(CylindricalCspropertyType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml"
