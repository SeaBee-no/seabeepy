from dataclasses import dataclass
from seabeepy.metadata.gmd.md_representative_fraction_type import MdRepresentativeFractionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRepresentativeFraction(MdRepresentativeFractionType):
    class Meta:
        name = "MD_RepresentativeFraction"
        namespace = "http://www.isotc211.org/2005/gmd"
