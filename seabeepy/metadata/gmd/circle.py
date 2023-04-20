from dataclasses import dataclass
from seabeepy.metadata.gmd.circle_type import CircleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Circle(CircleType):
    """A Circle is an arc whose ends coincide to form a simple closed loop.

    The three control points shall be distinct non-co-linear points for
    the circle to be unambiguously defined. The arc is simply extended
    past the third control point until the first control point is
    encountered.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
