from dataclasses import dataclass
from seabeepy.metadata.gmd.dq_completeness_commission_type import DqCompletenessCommissionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqCompletenessCommission(DqCompletenessCommissionType):
    class Meta:
        name = "DQ_CompletenessCommission"
        namespace = "http://www.isotc211.org/2005/gmd"
