from dataclasses import dataclass
from seabeepy.metadata.gmd.prime_meridian_property_type import PrimeMeridianPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianRef(PrimeMeridianPropertyType):
    class Meta:
        name = "primeMeridianRef"
        namespace = "http://www.opengis.net/gml"
