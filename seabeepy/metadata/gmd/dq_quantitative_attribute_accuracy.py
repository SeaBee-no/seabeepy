from dataclasses import dataclass
from seabeepy.metadata.gmd.dq_quantitative_attribute_accuracy_type import DqQuantitativeAttributeAccuracyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqQuantitativeAttributeAccuracy(DqQuantitativeAttributeAccuracyType):
    class Meta:
        name = "DQ_QuantitativeAttributeAccuracy"
        namespace = "http://www.isotc211.org/2005/gmd"
