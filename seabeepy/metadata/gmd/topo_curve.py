from dataclasses import dataclass
from seabeepy.metadata.gmd.topo_curve_type import TopoCurveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurve(TopoCurveType):
    """gml:TopoCurve represents a homogeneous topological expression, a
    sequence of directed edges, which if realised are isomorphic to a geometric
    curve primitive.

    The intended use of gml:TopoCurve is to appear within a line feature
    to express the structural and geometric relationships of this
    feature to other features via the shared edge definitions. If
    provided, the aggregationType attribute shall have the value
    “sequence”.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
