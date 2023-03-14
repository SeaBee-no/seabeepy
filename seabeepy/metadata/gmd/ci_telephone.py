from dataclasses import dataclass
from seabeepy.metadata.gmd.ci_telephone_type import CiTelephoneType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiTelephone(CiTelephoneType):
    class Meta:
        name = "CI_Telephone"
        namespace = "http://www.isotc211.org/2005/gmd"
