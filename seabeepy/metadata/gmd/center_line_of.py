from dataclasses import dataclass
from seabeepy.metadata.gmd.composite_curve_type import CurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CenterLineOf(CurvePropertyType):
    class Meta:
        name = "centerLineOf"
        namespace = "http://www.opengis.net/gml"
