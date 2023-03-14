from dataclasses import dataclass
from seabeepy.metadata.gmd.direct_position_type import DirectPositionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Pos(DirectPositionType):
    class Meta:
        name = "pos"
        namespace = "http://www.opengis.net/gml"
