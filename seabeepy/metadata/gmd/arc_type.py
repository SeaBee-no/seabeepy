from dataclasses import dataclass, field
from seabeepy.metadata.gmd.arc_string_type import ArcStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcType(ArcStringType):
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        }
    )
