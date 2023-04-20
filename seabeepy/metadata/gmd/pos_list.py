from dataclasses import dataclass
from seabeepy.metadata.gmd.direct_position_list_type import DirectPositionListType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PosList(DirectPositionListType):
    class Meta:
        name = "posList"
        namespace = "http://www.opengis.net/gml"
