from dataclasses import dataclass
from seabeepy.metadata.gmd.topo_curve_property_type import TopoCurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurveProperty(TopoCurvePropertyType):
    """
    The gml:topoCurveProperty property element may be used in features to
    express their relationship to the referenced topology edges.
    """
    class Meta:
        name = "topoCurveProperty"
        namespace = "http://www.opengis.net/gml"
