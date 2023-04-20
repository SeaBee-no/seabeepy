from dataclasses import dataclass
from seabeepy.metadata.gmd.dq_topological_consistency_type import DqTopologicalConsistencyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqTopologicalConsistency(DqTopologicalConsistencyType):
    class Meta:
        name = "DQ_TopologicalConsistency"
        namespace = "http://www.isotc211.org/2005/gmd"
