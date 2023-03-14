from dataclasses import dataclass
from seabeepy.metadata.gmd.topo_surface_property_type import TopoSurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceProperty(TopoSurfacePropertyType):
    """
    The gml:topoSurfaceProperty property element may be used in features to
    express their relationship to the referenced topology faces.
    """
    class Meta:
        name = "topoSurfaceProperty"
        namespace = "http://www.opengis.net/gml"
