from dataclasses import dataclass, field
from seabeepy.metadata.gmd.bspline_type import BsplineType
from seabeepy.metadata.gmd.curve_interpolation_type import CurveInterpolationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BezierType(BsplineType):
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        }
    )
    is_polynomial: bool = field(
        init=False,
        default=True,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        }
    )
