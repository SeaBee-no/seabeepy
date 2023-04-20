from dataclasses import dataclass
from seabeepy.metadata.gmd.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Value(MeasureType):
    """
    gml:value is a numeric value of an operation parameter, with its associated
    unit of measure.
    """
    class Meta:
        name = "value"
        namespace = "http://www.opengis.net/gml"
