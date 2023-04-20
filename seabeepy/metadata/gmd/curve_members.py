from dataclasses import dataclass
from seabeepy.metadata.gmd.curve_array_property_type import CurveArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveMembers(CurveArrayPropertyType):
    """This property element contains a list of curves.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """
    class Meta:
        name = "curveMembers"
        namespace = "http://www.opengis.net/gml"
