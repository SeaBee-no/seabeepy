from dataclasses import dataclass
from seabeepy.metadata.gmd.prime_meridian_property_type import PrimeMeridianPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridian2(PrimeMeridianPropertyType):
    """
    gml:primeMeridian is an association role to the prime meridian used by this
    geodetic datum.
    """
    class Meta:
        name = "primeMeridian"
        namespace = "http://www.opengis.net/gml"
