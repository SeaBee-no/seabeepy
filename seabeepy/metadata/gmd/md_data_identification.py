from dataclasses import dataclass
from seabeepy.metadata.gmd.md_data_identification_type import MdDataIdentificationType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDataIdentification(MdDataIdentificationType):
    class Meta:
        name = "MD_DataIdentification"
        namespace = "http://www.isotc211.org/2005/gmd"
