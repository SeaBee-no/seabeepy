from dataclasses import dataclass
from seabeepy.metadata.gmd.multi_curve_property_type import MultiCurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiEdgeOf(MultiCurvePropertyType):
    class Meta:
        name = "multiEdgeOf"
        namespace = "http://www.opengis.net/gml"
