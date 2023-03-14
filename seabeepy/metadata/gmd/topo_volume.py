from dataclasses import dataclass
from seabeepy.metadata.gmd.topo_volume_type import TopoVolumeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoVolume(TopoVolumeType):
    """gml:TopoVolume represents a homogeneous topological expression, a set of
    directed topologic solids, which if realised are isomorphic to a geometric
    solid primitive.

    The intended use of gml:TopoVolume is to appear within a solid
    feature to express the structural and geometric relationships of
    this solid feature to other features via the shared solid
    definitions.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
