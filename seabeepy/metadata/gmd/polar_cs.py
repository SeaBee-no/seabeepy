from dataclasses import dataclass
from seabeepy.metadata.gmd.polar_cstype import PolarCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCs(PolarCstype):
    """gml:PolarCS ia s two-dimensional coordinate system in which position is
    specified by the distance from the origin and the angle between the line
    from the origin to a point and a reference direction.

    A PolarCS shall have two gml:axis property elements.
    """
    class Meta:
        name = "PolarCS"
        namespace = "http://www.opengis.net/gml"
