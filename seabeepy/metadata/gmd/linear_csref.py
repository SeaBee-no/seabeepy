from dataclasses import dataclass
from seabeepy.metadata.gmd.linear_csproperty_type import LinearCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearCsref(LinearCspropertyType):
    class Meta:
        name = "linearCSRef"
        namespace = "http://www.opengis.net/gml"
