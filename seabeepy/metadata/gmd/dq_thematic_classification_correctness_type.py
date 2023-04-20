from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_dq_thematic_accuracy_type import AbstractDqThematicAccuracyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqThematicClassificationCorrectnessType(AbstractDqThematicAccuracyType):
    class Meta:
        name = "DQ_ThematicClassificationCorrectness_Type"
