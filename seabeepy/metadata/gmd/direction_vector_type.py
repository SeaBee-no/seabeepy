from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.angle_type import AngleType
from seabeepy.metadata.gmd.vector import Vector

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionVectorType:
    """
    Direction vectors are specified by providing components of a vector.
    """
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    horizontal_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "horizontalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_angle: Optional[AngleType] = field(
        default=None,
        metadata={
            "name": "verticalAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
