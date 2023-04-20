from dataclasses import dataclass, field
from seabeepy.metadata.gmd.arc_string_by_bulge_type import ArcStringByBulgeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByBulgeType(ArcStringByBulgeType):
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )
