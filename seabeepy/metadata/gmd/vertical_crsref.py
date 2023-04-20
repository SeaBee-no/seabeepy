from dataclasses import dataclass
from seabeepy.metadata.gmd.vertical_crsproperty_type import VerticalCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrsref(VerticalCrspropertyType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml"
