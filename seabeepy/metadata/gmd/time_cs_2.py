from dataclasses import dataclass
from seabeepy.metadata.gmd.time_csproperty_type import TimeCspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCs2(TimeCspropertyType):
    """
    gml:timeCS is an association role to the time coordinate system used by
    this CRS.
    """
    class Meta:
        name = "timeCS"
        namespace = "http://www.opengis.net/gml"
