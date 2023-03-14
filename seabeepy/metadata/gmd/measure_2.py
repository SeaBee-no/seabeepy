from dataclasses import dataclass
from seabeepy.metadata.gmd.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Measure2(MeasureType):
    """
    The value of a physical quantity, together with its unit.
    """
    class Meta:
        name = "measure"
        namespace = "http://www.opengis.net/gml"
