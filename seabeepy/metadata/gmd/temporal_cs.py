from dataclasses import dataclass
from seabeepy.metadata.gmd.temporal_cstype import TemporalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalCs(TemporalCstype):
    class Meta:
        name = "TemporalCS"
        namespace = "http://www.opengis.net/gml"
