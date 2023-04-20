from dataclasses import dataclass
from seabeepy.metadata.gmd.ex_temporal_extent_type import ExTemporalExtentType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExTemporalExtent(ExTemporalExtentType):
    class Meta:
        name = "EX_TemporalExtent"
        namespace = "http://www.isotc211.org/2005/gmd"
