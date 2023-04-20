from dataclasses import dataclass
from seabeepy.metadata.gmd.time_csproperty_type import TimeCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesTimeCs(TimeCspropertyType):
    class Meta:
        name = "usesTimeCS"
        namespace = "http://www.opengis.net/gml"
