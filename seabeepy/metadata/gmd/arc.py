from dataclasses import dataclass
from seabeepy.metadata.gmd.arc_type import ArcType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Arc(ArcType):
    """An Arc is an arc string with only one arc unit, i.e. three control
    points including the start and end point.

    As arc is an arc string consisting of a single arc, the attribute
    “numArc” is fixed to "1".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
