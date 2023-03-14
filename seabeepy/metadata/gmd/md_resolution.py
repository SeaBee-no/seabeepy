from dataclasses import dataclass
from seabeepy.metadata.gmd.md_resolution_type import MdResolutionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdResolution(MdResolutionType):
    class Meta:
        name = "MD_Resolution"
        namespace = "http://www.isotc211.org/2005/gmd"
