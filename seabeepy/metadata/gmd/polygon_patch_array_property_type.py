from dataclasses import dataclass
from seabeepy.metadata.gmd.surface_patch_array_property_type import SurfacePatchArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    gml:PolygonPatchArrayPropertyType provides a container for an array of
    polygon patches.
    """
