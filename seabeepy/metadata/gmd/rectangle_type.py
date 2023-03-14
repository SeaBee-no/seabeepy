from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_surface_patch_type import AbstractSurfacePatchType
from seabeepy.metadata.gmd.exterior import Exterior
from seabeepy.metadata.gmd.surface_interpolation_type import SurfaceInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectangleType(AbstractSurfacePatchType):
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        }
    )
