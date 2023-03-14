from dataclasses import dataclass
from seabeepy.metadata.gmd.multi_point_property_type import MultiPointPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiLocation(MultiPointPropertyType):
    class Meta:
        name = "multiLocation"
        namespace = "http://www.opengis.net/gml"
