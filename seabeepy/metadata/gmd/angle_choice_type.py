from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.angle_2 import Angle2
from seabeepy.metadata.gmd.dms_angle import DmsAngle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleChoiceType:
    angle: Optional[Angle2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    dms_angle: Optional[DmsAngle] = field(
        default=None,
        metadata={
            "name": "dmsAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
