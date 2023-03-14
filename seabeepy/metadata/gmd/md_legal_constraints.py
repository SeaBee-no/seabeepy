from dataclasses import dataclass
from seabeepy.metadata.gmd.md_legal_constraints_type import MdLegalConstraintsType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdLegalConstraints(MdLegalConstraintsType):
    class Meta:
        name = "MD_LegalConstraints"
        namespace = "http://www.isotc211.org/2005/gmd"
