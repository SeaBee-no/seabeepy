from dataclasses import dataclass
from seabeepy.metadata.gmd.polygon_patch_array_property_type import PolygonPatchArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatches(PolygonPatchArrayPropertyType):
    class Meta:
        name = "polygonPatches"
        namespace = "http://www.opengis.net/gml"
