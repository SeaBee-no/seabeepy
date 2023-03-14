from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_discrete_coverage_type import AbstractDiscreteCoverageType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridCoverageType(AbstractDiscreteCoverageType):
    pass
