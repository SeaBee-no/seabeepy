from dataclasses import dataclass
from seabeepy.metadata.gmd.multiplicity_type import MultiplicityType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Multiplicity(MultiplicityType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
