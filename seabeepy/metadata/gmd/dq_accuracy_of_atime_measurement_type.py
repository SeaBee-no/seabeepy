from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_dq_temporal_accuracy_type import AbstractDqTemporalAccuracyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqAccuracyOfAtimeMeasurementType(AbstractDqTemporalAccuracyType):
    class Meta:
        name = "DQ_AccuracyOfATimeMeasurement_Type"
