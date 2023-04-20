from dataclasses import dataclass
from seabeepy.metadata.gmd.dq_quantitative_result_type import DqQuantitativeResultType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqQuantitativeResult(DqQuantitativeResultType):
    class Meta:
        name = "DQ_QuantitativeResult"
        namespace = "http://www.isotc211.org/2005/gmd"
