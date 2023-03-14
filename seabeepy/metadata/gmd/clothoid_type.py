from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from seabeepy.metadata.gmd.abstract_curve_segment_type import AbstractCurveSegmentType
from seabeepy.metadata.gmd.affine_placement import AffinePlacement
from seabeepy.metadata.gmd.curve_interpolation_type import CurveInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ClothoidType(AbstractCurveSegmentType):
    ref_location: Optional["ClothoidType.RefLocation"] = field(
        default=None,
        metadata={
            "name": "refLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    scale_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    start_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "startParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    end_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "endParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CLOTHOID,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class RefLocation:
        affine_placement: Optional[AffinePlacement] = field(
            default=None,
            metadata={
                "name": "AffinePlacement",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml",
                "required": True,
            }
        )
