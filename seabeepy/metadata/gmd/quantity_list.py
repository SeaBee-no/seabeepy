from dataclasses import dataclass
from seabeepy.metadata.gmd.measure_or_nil_reason_list_type import MeasureOrNilReasonListType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityList(MeasureOrNilReasonListType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
