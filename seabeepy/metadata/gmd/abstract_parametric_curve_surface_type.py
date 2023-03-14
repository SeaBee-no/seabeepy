from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_surface_patch_type import AbstractSurfacePatchType
from seabeepy.metadata.gmd.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractParametricCurveSurfaceType(AbstractSurfacePatchType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
