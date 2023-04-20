from dataclasses import dataclass
from seabeepy.metadata.gmd.vertical_csproperty_type import VerticalCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalCs(VerticalCspropertyType):
    class Meta:
        name = "usesVerticalCS"
        namespace = "http://www.opengis.net/gml"
