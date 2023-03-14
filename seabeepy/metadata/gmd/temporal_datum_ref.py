from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_crstype import TemporalDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumRef(TemporalDatumPropertyType):
    class Meta:
        name = "temporalDatumRef"
        namespace = "http://www.opengis.net/gml"
