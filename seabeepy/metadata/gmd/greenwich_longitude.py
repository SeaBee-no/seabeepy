from dataclasses import dataclass
from seabeepy.metadata.gmd.angle_type import AngleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GreenwichLongitude(AngleType):
    """gml:greenwichLongitude is the longitude of the prime meridian measured
    from the Greenwich meridian, positive eastward.

    If the value of the prime meridian “name” is "Greenwich" then the
    value of greenwichLongitude shall be 0 degrees.
    """
    class Meta:
        name = "greenwichLongitude"
        namespace = "http://www.opengis.net/gml"
