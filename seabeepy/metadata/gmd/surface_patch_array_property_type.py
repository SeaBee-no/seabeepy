from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.cone import Cone
from seabeepy.metadata.gmd.cylinder import Cylinder
from seabeepy.metadata.gmd.polygon_patch import PolygonPatch
from seabeepy.metadata.gmd.rectangle import Rectangle
from seabeepy.metadata.gmd.sphere import Sphere
from seabeepy.metadata.gmd.triangle import Triangle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfacePatchArrayPropertyType:
    """
    gml:SurfacePatchArrayPropertyType is a container for a sequence of surface
    patches.
    """
    sphere: List[Sphere] = field(
        default_factory=list,
        metadata={
            "name": "Sphere",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cylinder: List[Cylinder] = field(
        default_factory=list,
        metadata={
            "name": "Cylinder",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    cone: List[Cone] = field(
        default_factory=list,
        metadata={
            "name": "Cone",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    rectangle: List[Rectangle] = field(
        default_factory=list,
        metadata={
            "name": "Rectangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    triangle: List[Triangle] = field(
        default_factory=list,
        metadata={
            "name": "Triangle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    polygon_patch: List[PolygonPatch] = field(
        default_factory=list,
        metadata={
            "name": "PolygonPatch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
