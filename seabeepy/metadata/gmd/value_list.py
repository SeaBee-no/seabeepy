from dataclasses import dataclass
from seabeepy.metadata.gmd.measure_list_type import MeasureListType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValueList(MeasureListType):
    """gml:valueList is an ordered sequence of two or more numeric values of an
    operation parameter list, where each value has the same associated unit of
    measure.

    An element of this type contains a space-separated sequence of
    double values.
    """
    class Meta:
        name = "valueList"
        namespace = "http://www.opengis.net/gml"
