from dataclasses import dataclass
from seabeepy.metadata.gmd.surface_patch_array_property_type import SurfacePatchArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    gml:TrianglePatchArrayPropertyType provides a container for an array of
    triangle patches.
    """
