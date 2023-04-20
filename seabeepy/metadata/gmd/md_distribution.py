from dataclasses import dataclass
from seabeepy.metadata.gmd.md_distribution_type import MdDistributionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistribution(MdDistributionType):
    class Meta:
        name = "MD_Distribution"
        namespace = "http://www.isotc211.org/2005/gmd"
