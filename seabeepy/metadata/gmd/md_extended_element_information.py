from dataclasses import dataclass
from seabeepy.metadata.gmd.md_extended_element_information_type import MdExtendedElementInformationType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdExtendedElementInformation(MdExtendedElementInformationType):
    class Meta:
        name = "MD_ExtendedElementInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
