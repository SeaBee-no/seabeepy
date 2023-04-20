from dataclasses import dataclass
from seabeepy.metadata.gmd.dq_conceptual_consistency_type import DqConceptualConsistencyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqConceptualConsistency(DqConceptualConsistencyType):
    class Meta:
        name = "DQ_ConceptualConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
