from dataclasses import dataclass
from seabeepy.metadata.gmd.time_edge_property_type import TimePrimitivePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValidTime(TimePrimitivePropertyType):
    """
    gml:validTime is a convenience property element.
    """
    class Meta:
        name = "validTime"
        namespace = "http://www.opengis.net/gml"
